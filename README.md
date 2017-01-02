<a href="https://github.com/LPRDev/RoverSentry/blob/master/images/RoverSentry_1.png">
<img src="https://github.com/LPRDev/RoverSentry/blob/master/images/RoverSentry_small.png" align="right">
</a>
# RoverSentry 
An autonomous land based drone utilizing ArduPilot and RaspberryPi.
----

RoverSentry is a project that will transform a standard RC Car into robotic sentry that will circle a property and take pictures of any suspicious activity it encounters. 
Once programmed with the patrol path the RoverSentry is autonomous and will continue its patrol until the entire patrol path has been traversed. 
A web application will be created that will be able to view live video from the rover at any time, snap and upload pictures, and take control of the Rover.

RoverSentry utilizes the [arduroverRS](https://github.com/LPRDev/ardupilotRS) project (a fork of the ardurover projet) but adds a Raspberry Pi for taking video/still picutres, and adding sensors (heat, movement, light, etc). A Turnigy Buggy (RC Car) will be modified to house an autopilot controller board along with the Raspberry Pi, a GPS receiver, a Camera with night vision, and sensors, raspicam. 

View the [RoverSentry wiki](https://github.com/LPRDev/RoverSentry/wiki) for further detials.
<a href="https://github.com/LPRDev/RoverSentry/blob/master/images/Mission%20Planner/MissionPlanner_1.jpg">
<img src="https://github.com/LPRDev/RoverSentry/blob/master/images/Mission%20Planner/MissionPlanner_1.jpg" align="right" width="40%"  height="40%" >
</a>
Planned Support for autopilot controller boards:

* APM 2.6


RoverSentry will require a mission planner (e.g. [Mission Planner](http://ardupilot.org/planner/index.html)) to load waypoints for property bounderies. Once the waypoints are loaded and the is autopilot is armed, the Roversentry will start its rounds.

<a href="https://github.com/LPRDev/RoverSentry/blob/master/images/Webapp/web_app_tablet2.png">
<img src="https://github.com/LPRDev/RoverSentry/blob/master/images/Webapp/web_app_tablet2.png" align="left" width="30%"  height="30%" >
</a>
The RoverSentry web app will provide a graphical user interface to view a live video feed from the drone, and give the ability to execute basic functions including photo taking, photo management, and path redirection.

This project is a work in progress. No operational code is available at this point in time.
