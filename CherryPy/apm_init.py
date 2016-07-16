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
from dronekit import connect, VehicleMode, LocationGlobal
import time, string, cherrypy, usb, socket, sys
class APM26(object):	
# Check for APM over usb port.
	APM_usb_VendorID=0x2341 #use specific ID for the curren APM (May change with other APM modules)
	APM_usb_ProductID=0x0010
	connected = False
	found = False
	status = "APM Not Started"
	# Use the test SITL vehicle so we can get a verhicle refernce bdfore attempting to connect
	# Note SITL must be started previously using dronekit-sitl rover-2.50
	print "Looking to see if the Dronekit vehicle simulator is running (SITL) ...."
	try:
		vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
	except:
		print "SITL not present, looking for APM" 
	# Check the APM module connection by seeing if the USB id of the APM shows up in the USB device list
	# If it is connected then try to connect to the device using dronekit.connect()	
	def check(self):
		#vehicle = APM26.vehicle
		APM26.found = False # reset check for APM each time
		#APM_conn = APM26.APM_conn
		VendorID = APM26.APM_usb_VendorID
		ProductID = APM26.APM_usb_ProductID
		#Status=APM26.Status
		busses = usb.busses()
		for bus in busses:
			devices = bus.devices
			for dev in devices:
				if ((dev.idVendor==VendorID)and(dev.idProduct==ProductID)):
					APM26.found = True
					print "APM Found!"
			if(APM26.found == False):
				APM26.status="APM module not found: Is the APM connected via USB?"
				APM26.connected = False   #Set the APM connnection to flase so it get started next time
				print "%s" % APM26.status
				return False
			if(APM26.connected == False):
				try:
					print "Connecting to APM ..."
					APM26.vehicle = connect('/dev/ttyACM0',wait_ready=True)
					APM26.connected = True
					APM26.status="APM Found and connected!"
					print "Connetion Status = %s" % APM26.status
					print "APM connected = %s" % APM26.connected
					# Wait for vehicle to finish setup and get a GPS lock so we can set a new home location
					if APM26.vehicle.mode.name == "INITIALISING":
						print "Waiting for vehicle to initialise"
						time.sleep(1)
					#while APM26.vehicle.gps_0.fix_type < 2:
					#	print "Waiting for GPS...:", APM26.vehicle.gps_0.fix_type
					#	time.sleep(1)
					# modify the home location since ArduPilot sets it to the location when GPS lock is obtained.
					# We want the RoverSentry to return to the start location when it aborts the mission.
					APM26.vehicle.commands.download()
					APM26.vehicle.commands.wait_ready() # wait until download is complete.
					time.sleep(1)
					cmds=APM26.vehicle.commands	
					APM26.vehicle.home_location = LocationGlobal(cmds[1].x, cmds[1].y, cmds[1].z)
					#APM26.vehicle.commands.upload()
					#APM26.vehicle.flush()
					print "Initializing Home Waypoint to latitude = %s longitude = %s altitude = %s" % (cmds[1].x, cmds[1].y, cmds[1].z)
					return True
				except Exception as e:
					APM26.status="APM found, but error connecting to APM: Specific Error: %s" %e.message
					print "Error with APM connection: %s" % APM26.status
					APM26.connected = False
					return False