#serial_request.py
#Version:	 2.1
#Author:	Peter Reinert
#Date:		1/23/2016          
      
import time
import serial
import sys
         
ser = serial.Serial(
              
	port='/dev/ttyAMA0',
	baudrate = 115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=5
)

process_stop = '0'
process_go = '1'
ack_success = 'OK'
command_success = 0      
exit_success = 1
exit_timeout = 2

message = 'Default'
command = '999'
timeout_limit = 12

# ping_Device()
# sends string 'ping' to device over UART
# other device will respond with ack_success 
# optional timer is commented out 
def ping_Device():
	print 'Finding Device...'
	ping_flag = 1
        ser.write('ping')
	ping = ser.readline()
	print ping
	current_time=time.time()
	#while(time.time() < current_time+5):
        if (ping == ack_success):
               	print 'Device found'
               	return 1
        print 'No device found'
        return 0

# send_Command
# requires 2 strings
#	message - displays to terminal
#	command - an integer in string format; to be interpreted by other device
# anything going over serial MUST by in string format
def send_Command(message, command):
	print message
        transfer_flag = 1
        timeout = time.time()+timeout_limit
        while (transfer_flag):
                ser.write(command)
                ack = ser.readline()
                if (ack):
                       print 'Success'
                       print ack
                       transfer_flag = 0
                if (time.time() > timeout):
                        print 'Failure: timeout'
                        exit(exit_timeout)

def main():
### Arguments
	if (len(sys.argv) < 2):
		print 'missing an argument'
		sys.exit()
	if (len(sys.argv) > 2):
        	print 'too many argument'
		sys.exit()

	ardu_command = sys.argv[1]
## give command and message
	if (ardu_command == 'pause'):
		message = 'Halting...'
		command = process_stop
	elif (ardu_command == 'resume'):
		message = 'Resuming...'
		command = process_go
	else:
		print 'invalid command'
		sys.exit()

### Send Command
	#device_available = ping_Device()
	#if (device_available == 0):
	#	exit(exit_timeout)
	#else:
	send_Command(message,command)
	exit(exit_success)
main()

###############################

#def ping_Device():
#	ping = ser.write('ping')
#	print 'Finding Device...'
#	if (ping): 
#		print 'Device found'
#		return 1
#	else: 
#		print 'No device found'
#		return 0

#def send_Command(message, command):
#	print message
#	transfer_flag = 1
#	timeout = time.time()+timeout_limit
#	while (transfer_flag):
#              	ser.write(process_stop)
#              	ack = ser.readline()
#              	if (len(ack)>0):
#                       print 'Success'
#                       print ack
#                       transfer_flag = 0
#		if (time.time() > timeout):
#			print 'Failure: timeout' 
#			exit(exit_timeout)
		


#if (ardu_command == 'stop'):
#	print 'Halting...'
#	transfer_flag = 1
#	while (transfer_flag):
#		ser.write(process_stop)
#		ack = ser.readline()
#		if (len(ack)>0):
#			print 'Success'
#			print ack
#			#transfer_flag = 0
#elif (ardu_command == 'go'):
#	print 'Resuming...'
#	transfer_flag = 1
#       while (transfer_flag):
#                ser.write(process_go)
#                ack = ser.readline()
#                if (len(ack)>0):
#                        print 'Success'
#                        print ack
#                        transfer_flag = 0
#else:
#	print 'invalid command'
#	sys.exit()


#recieve_flag=1	
#while (recieve_flag):
#	print 'Retrieving...\n'
#	ser.write('1') #signal testpi
#	ret_value = ser.readline() 
#	if (len(ret_value)>0): #exit upon recieving valid data
#		print 'Success\n'
#		print ret_value
#		recieve_flag=0
