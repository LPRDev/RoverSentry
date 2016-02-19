# PIR motion sensor script.
# Detects movement using a PIR module
#
# Source modified from original script by Matt Hawkins.
# 
 
# Import required Python libraries
import RPi.GPIO as GPIO
import time
import subprocess
import os
from datetime import datetime
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO to use on Pi
GPIO_PIR = 4
 
print "PIR Module Test (CTRL-C to exit)";
 
# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo
 
Current_State  = 0
Previous_State = 0
 
try:

    print "Waiting for PIR to settle ...";

    # Loop until PIR output is 0
    while GPIO.input(GPIO_PIR)==1:
        Current_State = 0;
        
    print "  Ready";
    
    # Open the toggle text file to check to turn auto on and off.
    # w+ modifier will create the file if it does not exist.
    toggle = open("/usr/share/RoverSentry/PIR/pir_sensor_auto.txt","w+");
        
    # Read the first digit of the text file.
    check = toggle.read(10);
    
    print "Read from " + toggle.name + " status: " + check + ".";

        # Loop until users quits with CTRL-C
    while True:
        
        # Read PIR state
        Current_State = GPIO.input(GPIO_PIR);

        if Current_State==1 and Previous_State==0:
            # PIR is triggered
            print "  Motion detected!";
            
            # If the toggle file is ON, take a photo.
            if check == "ON":
                print "#     Taking a snapshot... "
                now = datetime.now()
                time_stamp = str(now.month) + str(now.day) + str(now.year) + str(now.hour) + str(now.minute) + str(now.second)
                param_list = ["if=/dev/video0", " of=/var/www/html/photos/autosnapshot_" + time_stamp + ".jpeg", " bs=11M", " count=1"]
            
                print "#     dd if=/dev/video0 of=/var/www/html/photos/autosnapshot_" + time_stamp + ".jpeg bs=11M count=1";
        
                # Shell 
                os.system('sudo pkill uv4l');
                time.sleep(.1);
                os.system('uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg');
                time.sleep(.1);
                        
                # Take the photo
                os.system('dd ' + param_list[0] + param_list[1] + param_list[2] + param_list[3]);
            
                time.sleep(.1);
                os.system('sudo pkill uv4l');
                time.sleep(.1);
                os.system('uv4l --driver raspicam --auto-video_nr --width 640 --height 480 --encoding jpeg');
                print "#     Snapshot saved!";
            
            # Record previous state
            Previous_State=1;
        elif Current_State==0 and Previous_State==1:
            # PIR has returned to ready state
            print "  Ready";
            Previous_State=0;
            
            # Reposition pointer at the beginning once again
            toggle.seek(0, 0);
            
            # Read from the check toggle text file.
            check = toggle.read(10);
            print "Read from " + toggle.name + " status: " + check + ".";

            # Wait for 10 milliseconds
            time.sleep(0.01);

except KeyboardInterrupt:
    # Close the open toggle text file.
    print "Closing auto file.";
    toggle.close();
    print "  Quit";

    # Reset GPIO settings
    GPIO.cleanup()