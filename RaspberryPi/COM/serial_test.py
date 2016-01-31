#serial_test.py
#Version:	2.0
#Author:	Peter Reinert
#Date:		1/23/2016
      
import time
import serial
          
      
ser = serial.Serial(
              
	port='/dev/ttyAMA0',
	baudrate = 115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
counter=0
ready = 0;		# status of testpi (halt/resume)
valid = 0;		# able to send data
ack_success = 'OK'
process_stop = '0'
process_resume = '1'      


while 1:
	print counter
	if((counter>6) & (counter<20)): # condition required to send data
		valid = 1;
	else:
		valid = 0;	

	trig = ser.read() # get orders from raspberrypi
	if (ser.readline() == 'ping'):
		print 'pinged'
		if (valid): ser.write(ack_success)
		#else: ser.write(ack_success) 
	if ((valid) & (trig == process_stop)):
		print 'Halted'
		ready = 0;
		ser.write('Data flow halted')
	if((valid) & (trig == process_resume)):
		print 'Resuming'
		ready = 1;
		ser.write('Process Resumed')
	if ((valid) & (ready)):
		#ser.write('sample data')
		print 'sending data'

	time.sleep(0.3)
	counter += 1
	counter = counter % 20
