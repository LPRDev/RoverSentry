
# Problem:
Dronekit vehicle connection takes about 15 seconds to establish comminications with the APM module and needed a method of receiving calls from the RoveSentry web app.
One option was to look for simple Restful web server that could take care of the dronekit connection and provide an easy way to send messages to it.

# CherryPy
Enter [CherryPy](http://www.cherrypy.org/), which is a minimalist web server written in python. 
It can be used to provide a simple web page and also supports [Restful calls](http://docs.oracle.com/javaee/6/tutorial/doc/gijqy.html) 
for each of the methods exposed as a web service. The web page is very primitive so it does not replace the RoverSentry Web app. it compliments it.  

Since the Uv4L video streaming sevice uses port 8080 (which is also the default for CherryPy) the CherryPy port was relocated to port 9000. So to acess the page use:
```
http://RaspberryPyaddress:9000
```

# Startup
Placing a call into the dronekit_init.py within /etc/rc.local was the easist method of getting the CherryPy server up on startup.
Note: That because the dronekit takes 15 seconds to get a veihicle connection, the web page is not avialble for 15 seconds or so after the RaspberryPy starts (wich takes about 30 seconds on a RaspberryPy2 booting to a command line.


