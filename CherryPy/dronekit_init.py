# Version 1.0

from dronekit import connect, VehicleMode
#from droneapi import connect
import time
import string
import cherrypy
import usb

# Check for APM over usb port, if not present then wait for it to connection...
APM_usb_VendorID=0x2341
APM_usb_ProductID=0x0010
APM_found = False

while (APM_found==False):
	busses = usb.busses()
	for bus in busses:
		devices = bus.devices
		for dev in devices:
			if ((dev.idVendor==APM_usb_VendorID)and(dev.idProduct==APM_usb_ProductID)):
				APM_found = True
				print "APM Found!"
				break	
	if (APM_found==False):
		print " APM connection failure: Is the the APM USB connected to Raspberry Pi?"
	time.sleep(5)				
				
print "Connecting to APM module..."
# Now that we found it, connect to it
vehicle = connect('/dev/ttyACM0',wait_ready=True)
speed=0.5;


# Enable web server to be availble on all interfaces
cherrypy.config.update({'server.socket_host': '0.0.0.0'})
#move port to 9000 so it doesnt conflict with the video stream (UV4l)
cherrypy.config.update({'server.socket_port': 9000})



# Don't try anything until apm is ready
#vehicle.armed = True  
while not vehicle.armed:
        print " Waiting for vehicle to initialise..."
        time.sleep(1)

### Callbacks ###
#def groundspeed_callback(self, attr_name,value):
	#print "Ground Speed: %s" % self.groundspeed;
#vehicle.add_attribute_listener('groundspeed',groundspeed_callback);

#def location_callback(self, attr_name, value):
#	print "Location: %s" % self.location.global_frame;
#vehicle.add_attribute_listener('location.global_frame',location_callback);

# Battery Monitoring ....
# Allow both voltage only battery monitoring
vehicle.parameters['BATT_MONITOR']=4;

# add callback to see if the BATT_MONITOR changes# add callback to see if the BATT_MONITOR changes
#@vehicle.parameters.on_attribute('BATT_MONITOR')
#def Battert_param_callback(slef, attr_name, value):
#    print " Parameter BATT_MONITOR changed to : %s" % (attr_name,value)

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

class DroneControl(object):
    # Create a top level html page and supply function buttons
	@cherrypy.expose
	def index(self):
         return """<html>
		 <head></head>
          <body>
            <H1>Rover Sentry Control Page:</H1>
            <form action="status">
              <button type="submit">Status</button>
            </form>
            <form action="halt">
              <button type="submit">Halt</button>
            </form>
            <form action="resume">
              <button type="submit">Resume</button>
            </form>
            <form action="home">
              <button type="submit">Home</button>
            </form>
	    <form action="waypoints">
	      <button type="submit">Waypoints</button>
	    </form>
            <form action="exit">
              <button type="submit">Exit</button>
            </form>
          </body>
        </html>"""

	@cherrypy.expose
	def halt(self):
		vehicle.mode = VehicleMode("HOLD");
		vehicle.armed = False;
		vehicle.groundspeed = 0;
		vehicle.airspeed = 0;
		#    while vehicle.groundspeed > 0.1:
		#	vehicle.groundspeed = 0;
		#        	print "Waiting for groundspeed change"
		#        	time.sleep(1)  
		return "Vehicle Halted"
	@cherrypy.expose
	def resume(self):
		vehicle.armed = True;
		vehicle.mode = VehicleMode("AUTO");
		vehicle.groundspeed = speed;
		while vehicle.groundspeed < speed:
			vehicle.groundspeed = speed;
			print "Resuming...";
		return "Resume"

	@cherrypy.expose
	def waypoints(self):
		cmds = vehicle.commands;
		cmds.download();
		cmds.wait_ready() # wait until download is complete.
		wp_count = vehicle.commands.count;
		status= " WayPoint Count: %s <BR>" % wp_count 
		for waypnt in cmds:
		   status+= "%s <BR>" % waypnt; 
		status+= " Home Location: %s" % vehicle.home_location
		return status

	@cherrypy.expose
	def home(self):
		vehicle.armed = True;
		vehicle.mode = VehicleMode("RTL");
		vehicle.groundspeed = speed;
		while vehicle.groundspeed < speed:
			vehicle.groundspeed = speed;
		return "Going Home....";

	@cherrypy.expose
	def exit(self):
		vehicle.close();
		return "Closing the vehicle object"

	@cherrypy.expose
	def status(self):
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


if __name__ == '__main__':
    cherrypy.quickstart(DroneControl())
