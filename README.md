<a href="https://github.com/LPRDev/RoverSentry/blob/master/images/RoverSentry_1.png">
<img src="https://github.com/LPRDev/RoverSentry/blob/master/images/RoverSentry_small.png" align="right">
</a>
# RoverSentry 
An autonomous land based drone utilizing ArduPilot and RaspberryPi.
----

RoverSentry is a project that will transform a standard RC Car into robotic sentry that will circle a property and take pictures of any suspicious activity it encounters. 
Once programmed with the patrol path the RoverSentry is autonomous and will continue its patrol until the entire patrol path has been traversed. 
A web application will be created that will be able to view live video from the rover at any time, snap and upload pictures, and take control of the Rover.

RoverSentry is based upon the ArduRover project but adds a Raspberry Pi for taking video/still picutres, and adding sensors (heat, movement, light, etc). A Turnigy Buggy (RC Car) will be modified to house an autopilot controller board along with the Raspberry Pi, a GPS receiver, a Camera with night vision, and sensors, raspicam. 

View the [RoverSentry wiki](https://github.com/LPRDev/RoverSentry/wiki) for further detials.

Planned Support for autopilot controller boards:

* APM 2.6
* Navio 2

RoverSentry will require a mission planner (e.g. [APM Mission Planner 2.0](http://planner2.ardupilot.com/)) to load waypoints for property bounderies. Once the waypoints are loaded and the is autopilot is armed, the Roversentry will start its rounds.

This project is a work in progress. No operational code is available at this point in time.
