# Version 1.0

from dronekit import connect, VehicleMode, LocationGlobal
import time, string, cherrypy, usb, socket, sys
#from apm_init import APM26
from apm_init import *

# Enable web server to be availble on all interfaces
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
#move port to 9000 so it doesnt conflict with the video stream (UV4l)
cherrypy.config.update({'server.socket_port': 9000})

###############################################################################
# APM26
# Control class for interacting with the APM26 module on the Rover Sentry
# Requirements
# * Detects connection with APM26 over USB
# * Supports use of the Dronekit SITL for development (optional)
# * Creates a Dronekit vehicle object
# * Provides Status on the APM and Dronekit connections
# * Provides a vehicle object for the RoverSentry
###############################################################################	
#class APM26(object):	
# Check for APM over usb port.
#	APM_usb_VendorID=0x2341 #use specific ID for the curren APM (May change with other APM modules)
#	APM_usb_ProductID=0x0010
#	connected = False
#	found = False
#	status = "APM Not Started"
	# Use the test SITL vehicle so we can get a verhicle refernce bdfore attempting to connect
	# Note SITL must be started previously using dronekit-sitl rover-2.50
#	print "Looking to see if the Dronekit vehicle simulator is running (SITL) ...."
#	try:
#		vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
#	except:
#		print "SITL not present, looking for APM" 
	# Check the APM module connection by seeing if the USB id of the APM shows up in the USB device list
	# If it is connected then try to connect to the device using dronekit.connect()	
#	def check(self):
		#vehicle = APM26.vehicle
#		APM26.found = False # reset check for APM each time
		#APM_conn = APM26.APM_conn
#		VendorID = APM26.APM_usb_VendorID
#		ProductID = APM26.APM_usb_ProductID
		#Status=APM26.Status
#		busses = usb.busses()
#		for bus in busses:
#			devices = bus.devices
#			for dev in devices:
#				if ((dev.idVendor==VendorID)and(dev.idProduct==ProductID)):
#					APM26.found = True
#					print "APM Found!"
#			if(APM26.found == False):
#				APM26.status="APM module not found: Is the APM connected via USB?"
#				APM26.connected = False   #Set the APM connnection to flase so it get started next time
#				print "%s" % APM26.status
#				return False
#			if(APM26.connected == False):
#				try:
#					print "Connecting to APM ..."
#					APM26.vehicle = connect('/dev/ttyACM0',wait_ready=True)
#					APM26.connected = True
#					APM26.status="APM Found and connected!"
#					print "Connetion Status = %s" % APM26.status
#					print "APM connected = %s" % APM26.connected
					# Wait for vehicle to finish setup and get a GPS lock so we can set a new home location
#					while APM26.vehicle.mode.name == "INITIALISING":
#						print "Waiting for vehicle to initialise"
#						time.sleep(1)
					#while not APM26.vehicle.home_location:
					#	cmds = APM26.vehicle.commands
					#	cmds.download()
					#	cmds.wait_ready()
					#	print "waiting for home location to be set...."
					#	time.sleep(1)
#					APM26.vehicle.parameters['THR_MAX']=25
#					return True
#				except Exception as e:
#					APM26.status="APM found, but error connecting to APM: Specific Error: %s" %e.message
#					print "Error with APM connection: %s" % APM26.status
#					APM26.connected = False
#					return False

#def wildcard_callback(self, attr_name, value):
#    print "Attribute  %s = %s" % (attr_name, value)
#    vehicle = self; # not needed, just wanted to see if there was a difference
#vehicle.add_attribute_listener('*',wildcard_callback);

#def battery_callback(self, attr_name, value):
#       if self.battery.level < 33:
#			vehicle.mode = VehicleMode("RTL");
#			print "Battery Level Alert: Less than 33%, returning to launch";

#vehicle.add_attribute_listener('battery',battery_callback);

#	def groundspeed_callback(self, attr_name,value):
#        	print "Ground Speed: %d" % value;
#
#	vehicle.add_attribute_listener('groundspeed',groundspeed_callback);


#
#	vehicle.add_attribute_listener('groundspeed',groundspeed_callback);
#APM26.vehicle.add_attribute_listener('gps_0',gps_callback);

#def gps_callback(self, attr_name,value):
# 	print "GPS stuff: %s" % value;
	
###############################################################################
# DroneControl
# This class is used as the main service on the RaspberryPi for the RoverSentry
# Requirements
# * Provide a basic web page for control: availble at the URL:
#    <raspberrypiaddress>:9000 on your web browser
# * Detect connection for APM module and provide status on webpage if 
#    theres a problem with the connection
# * Provide status and diagnotic info during feild tests
# * Provide basic RoverSentry control (Start , Halt, continue)
###############################################################################	
class DroneControl(object):
	apm_module=APM26()
	speed = 0.5
	# Create APM connection on CherryPy startup...
	apm_module.check()
	# Create a top level html page and supply function buttons
	@cherrypy.expose
	def index(self):
		DroneControl.apm_module.check()
		print"module = %s and connection = %s " % (DroneControl.apm_module.found,DroneControl.apm_module.connected)
		print"APM Status %s" % DroneControl.apm_module.status
		if ((DroneControl.apm_module.connected == False)or(DroneControl.apm_module.found == False)):
			msg="<html><head></head><body><H2>Error connecting to APM module!</H2>"
			msg+="Error: %s" % APM26.status
			msg+="<form action=\"connect\"> <button type=\"submit\"> Retry</button></form>"
			return msg
		else:	
			return """<html>
		 <head></head>
          <body>
            <H1>Rover Sentry Control Page:</H1>
			<BR><form action="status">
              <button type="submit">Status</button>
            </form>
            <BR><form action="halt">
              <button type="submit">Halt</button>
            </form>
            <BR><form action="resume">
              <button type="submit">Resume</button>
            </form>
            <BR><form action="home">
              <button type="submit">Home</button>
            </form>
			<BR><form action="setHome">
              <button type="submit">setHome</button>
            </form>
			<BR><form action="setNext">
			  <input type="text" value="1" name="next" />
              <button type="submit">setNext</button>
            </form>
			<BR><form action="waypoints">
			  <button type="submit">Waypoints</button>
			</form>
            <BR><form action="exit">
              <button type="submit">Exit</button>
            </form>
          </body>
        </html>"""
		
	###########################################################################
	# Set the Next location of the mission. 
	# 
	###########################################################################
	@cherrypy.expose
	def setNext(self, next=1): 
		next=int(next)
		status="Next not set"
		print " APM Next = %d" % APM26.vehicle.commands.next
		print " Next = %d" % next
		if (next == APM26.vehicle.commands.next):
			status="Next already set to waypoint %s" % next
			return status
		try:
			APM26.vehicle.commands.download()
			APM26.vehicle.commands.wait_ready() # wait until download is complete.
			cmds=APM26.vehicle.commands
			cmds=APM26.vehicle.commands
			if (next > cmds.count):
				status="You can't set a waypoint to one that doesn't exist. Max wapypoint is: %s and you selected %s" % (cmds.count, next)
				return status
			status = "Next waypoint has been set to waypoint %s located at %s" %  (next, cmds[next])
		except Exception as e:
			status="Error setting Next: Specific Error: %s" %e.message
		return status
	###########################################################################
	# Set the Home location to the first Waypoint. 
	# Needs to wait for 3 GPS beofre it can be set
	###########################################################################
	@cherrypy.expose
	def setHome(self):
		status="Home not set"
		if (APM26.vehicle.gps_0.fix_type < 3):
			status+=" due to poor GPS reception." 
			status+="<BR> Number of GPS locks = %s" % APM26.vehicle.gps_0.fix_type
			return status
		try:
			APM26.vehicle.commands.download()
			APM26.vehicle.commands.wait_ready() # wait until download is complete.
			cmds=APM26.vehicle.commands
			status = "Home hase been set to : %s" %  APM26.vehicle.home_location
			status +="<BR>Here is the current location: %s" % APM26.vehicle.location.global_frame
			status+="<BR> Number of GPS locks = %s" % APM26.vehicle.gps_0.fix_type
		except Exception as e:
			status="Error setting home: Specific Error: %s" %e.message
		return status
		
	def setwaypoint(self):
		#APM26.vehicle.commands.download()
		#APM26.vehicle.commands.wait_ready() # wait until download is complete.
		#cmds=APM26.vehicle.commands
		#APM26.vehicle.home_location = LocationGlobal(cmds[1].x, cmds[1].y, cmds[1].z)
		APM26.vehicle.home_location = APM26.vehicle.location.global_frame
		#APM26.vehicle.commands.upload()
		#print "Initializing Home Waypoint to latitude = %s longitude = %s altitude = %s" % (cmds[1].x, cmds[1].y, cmds[1].z)
		#time.sleep(3)
	###########################################################################
	# Check to see if APM module is there and refresh the page right after
	###########################################################################
	@cherrypy.expose
	def connect(self):
		DroneControl.apm_module.check()
		ip = socket.gethostname()
		msg = "<html> <body> <script type=\"text/javascript\"> window.location.replace(\"http://%s:9000\");  </SCRIPT></body></html>" % ip
		print "url=%s" % msg
		return msg
	###########################################################################
	# Stop the Rover wherever it is
	###########################################################################
	@cherrypy.expose
	def halt(self):
		DroneControl.apm_module.vehicle.mode = VehicleMode("HOLD");
		DroneControl.apm_module.vehicle.armed = False;
		DroneControl.apm_module.vehicle.groundspeed = 0;
		DroneControl.apm_module.vehicle.airspeed = 0;
		#    while vehicle.groundspeed > 0.1:
		#	vehicle.groundspeed = 0;
		#        	print "Waiting for groundspeed change"
		#        	time.sleep(1)  
		return "Vehicle Halted"
	############################################################################	
	# Start or Continue the mission (after a Halt)
	############################################################################
	@cherrypy.expose
	def resume(self):
		DroneControl.apm_module.vehicle.armed = True;
		DroneControl.apm_module.vehicle.mode = VehicleMode("AUTO");
		DroneControl.apm_module.vehicle.groundspeed = DroneControl.speed;
		while DroneControl.apm_module.vehicle.groundspeed < DroneControl.speed:
			DroneControl.apm_module.vehicle.groundspeed = DroneControl.speed;
			time.sleep(1)
			print "Resuming...";
		return "Resume"
	###########################################################################
	# Reteive Mission (waypoints) from APM module and list on the webpage 
	###########################################################################
	@cherrypy.expose
	def waypoints(self):
		vehicle = APM26.vehicle
		DroneControl.apm_module.vehicle.commands.download()
		DroneControl.apm_module.vehicle.commands.wait_ready()
		cmds = DroneControl.apm_module.vehicle.commands
		wp_count = vehicle.commands.count;
		msg= "<H1>Rover Sentry Mission (Waypoints)</H1>"
		msg+= " WayPoint Count: %s <BR>" % wp_count 
		counter=0;
		for waypnt in cmds:
			msg+= "    Waypoint %s:" % counter;
			msg+= " : %s ," % waypnt.x; 
			msg+= " longitude: %s " % waypnt.y;
			msg+= " altitude: %s <BR>" % waypnt.z;
			counter += 1
		#APM26.vehicle.home_location = LocationGlobal(cmds[1].x, cmds[1].y, cmds[1].z)
		msg+= " Home Location: %s <BR>" % vehicle.home_location
		msg+= "Current Location: %s <BR>" % vehicle.location.global_frame
		msg+= "Next Waypoint location is Waypoint %s located at lat=%s lon=%s, Alt=%s <BR>" % (cmds.next , cmds[cmds.next].x, cmds[cmds.next].y, cmds[cmds.next].z)
		
		return msg
	###########################################################################
	# Return to home (Set at Waypint 1 in APM26)
	###########################################################################
	@cherrypy.expose
	def home(self):
		DroneControl.apm_module.vehicle.armed = True;
		DroneControl.apm_module.vehicle.mode = VehicleMode("RTL");
		DroneControl.apm_module.vehicle.groundspeed = DroneControl.speed;
		while DroneControl.apm_module.vehicle.groundspeed < DroneControl.speed:
			DroneControl.apm_module.vehicle.groundspeed = DroneControl.speed;
		return "Going Home....";
	###########################################################################
	# Shutdown the Dronekit Vehicle (Saves power when waiting for use)
	# Use Resume to start up again (will take 15 seconds or more)
	###########################################################################
	@cherrypy.expose
	def exit(self):
		DroneControl.apm_module.vehicle.close();
		APM26.connected = False
		return "Closing the vehicle object"
	###########################################################################
	# List every last bit of status from Dronelit or other sources.
	# Useful for debugging in the feild
	###########################################################################
	@cherrypy.expose
	def status(self):
		vehicle = DroneControl.apm_module.vehicle
		cmds = vehicle.commands;
		cmds.download();
		cmds.wait_ready() # wait until download is complete.
		wp_count = vehicle.commands.count;
		#return "Armed: %s \nBattery: %s \nWaypoints: %d \nStatus: %s" % (vehicle.armed,vehicle.battery, wp_count, vehicle.system_status)
		#return "Armed: %s \nWaypoints: %d" % (vehicle.armed, wp_count)
		#return "Status: %s" %(vehicle.system_status)
		status= "<html><body>"
		status+= "<H1>Rover Sentry Status</H1>"
		status+= "<H2><a href=\" http://python.dronekit.io/automodule.html\">Dronekit Attributes </a></H2><BR>"
		status+= " Battery volatge: %s <BR>" % vehicle.battery.voltage
 		status+= "    Bateery current (millamps): %s <BR>" % vehicle.battery.current
		status+= "    Battery level: %s <BR>" % vehicle.battery.level
		status+= " Global Location: %s <BR>" % vehicle.location.global_frame
		status+= " Global Location (relative altitude): %s <BR>" % vehicle.location.global_relative_frame
		status+= " Local Location: %s <BR>" % vehicle.location.local_frame
		status+= " Attitude: %s <BR>" % vehicle.attitude
		status+= " Velocity: %s <BR>" % vehicle.velocity
		status+= " GPS: %s <BR>" % vehicle.gps_0
		status+= " Gimbal status: %s <BR>" % vehicle.gimbal
		status+= " Last Heartbeat: %s <BR>" % vehicle.last_heartbeat
		status+= " Rangefinder: %s <BR>" % vehicle.rangefinder
		status+= " Rangefinder distance: %s <BR>" % vehicle.rangefinder.distance
		status+= " Rangefinder voltage: %s <BR>" % vehicle.rangefinder.voltage
		status+= " Heading: %s <BR>" % vehicle.heading
		status+= " Is Armable?: %s <BR>" % vehicle.is_armable
		status+= " System status: %s <BR>" % vehicle.system_status.state
		status+= " Groundspeed: %s <BR>" % vehicle.groundspeed    # settable
		status+= " Airspeed: %s <BR>" % vehicle.airspeed    # settable
		status+= " Mode: %s <BR>" % vehicle.mode.name    # settable
		status+= " Armed: %s <BR>" % vehicle.armed    # settable		
		status+= " WayPoint Count: %s <BR>" % wp_count 
		for waypnt in cmds:
		   status+= "%s <BR>" % waypnt; 
		status+= " Home Location: %s" % vehicle.home_location   
		status+= " Autopilot Firmware version: %s <BR>" % vehicle.version
		status+= "   Major version number: %s <BR> " % vehicle.version.major
		status+= "   Minor version number: %s  <BR>" % vehicle.version.minor
		status+= "   Patch version number: %s  <BR>" % vehicle.version.patch
		status+= "   Release type: %s  <BR>" % vehicle.version.release
		status+= "   Release version: %s  <BR>" % vehicle.version.release_version()
		status+= "   Stable release?: %s  <BR>" % vehicle.version.is_stable()		
		status+= " Autopilot capabilities  <BR>"
		status+= "   Supports MISSION_FLOAT message type: %s  <BR>" % vehicle.capabilities.mission_float
		status+= "   Supports PARAM_FLOAT message type: %s  <BR>" % vehicle.capabilities.param_float
		status+= "   Supports MISSION_INT message type: %s <BR>" % vehicle.capabilities.mission_int
		status+= "   Supports COMMAND_INT message type: %s <BR>" % vehicle.capabilities.command_int
		status+= "   Supports PARAM_UNION message type: %s <BR>" % vehicle.capabilities.param_union
		status+= "   Supports ftp for file transfers: %s <BR>" % vehicle.capabilities.ftp
		status+= "   Supports commanding attitude offboard: %s <BR>" % vehicle.capabilities.set_attitude_target
		status+= "   Supports commanding position and velocity targets in local NED frame: %s <BR>" % vehicle.capabilities.set_attitude_target_local_ned
		status+= "   Supports set position + velocity targets in global scaled integers: %s <BR>" % vehicle.capabilities.set_altitude_target_global_int
		status+= "   Supports terrain protocol / data handling: %s <BR>" % vehicle.capabilities.terrain
		status+= "   Supports direct actuator control: %s <BR>" % vehicle.capabilities.set_actuator_target
		status+= "   Supports the flight termination command: %s <BR>" % vehicle.capabilities.flight_termination
		status+= "   Supports mission_float message type: %s <BR>" % vehicle.capabilities.mission_float
		status+= "   Supports onboard compass calibration: %s <BR>" % vehicle.capabilities.compass_calibration
		status+= " EKF OK?: %s <BR>" % vehicle.ekf_ok
 		# prints out  parameters found here: http://ardupilot.org/rover/docs/parameters.html
		status+= "<H2><a href=\"http://ardupilot.org/copter/docs/parameters.html\"> Dronekit Parameters </a></H2><BR>"
		for key, value in vehicle.parameters.iteritems():
			status+= "\n\r * Key:%s Value:%s <BR>" % (key,value)
		status+= "</body></html>"
		return status

	

# Start the RoverSentry DronConrol CherryPy Web application
if __name__ == '__main__':
    cherrypy.quickstart(DroneControl())

