'''
' connection class takes an object from the serial library
' and send some data to serial port which in our case an arduino nano
' clean_path is a function we made to send the path in a suitable form
' connect is a function that sends the data
'''
# import pyserial library, and time library will be used for sleep
import serial, time
class arduino_connection(object):
	'''
	' Our beatiful constructor takes the path and port
	'''
	def __init__(self, path, port):
		self.path = path
		self.port = port
		self.speed = 9600
	'''
	' clean_path is a function that get rid off some staff we don't need
	' and returns a clean path ready to send to arduino
	'''
	def clean_path(self, old_path):
		# convert the list to string
	    path_to_ard = str(self.path)
	    # iterate over the list to eliminate brackets and parantesess
	    for i in ["[","]","("," "] :  
	        path_to_ard = path_to_ard.replace(i,"")
	    path_to_ard = path_to_ard.replace("),", ":")
	    path_to_ard = path_to_ard.replace(")", "")
	    # concatenate a $ symbol just to let arduino know the end of receive
	    path_to_ard = path_to_ard + "$"
	    return path_to_ard
	'''
	' connect is a function that sends the data to arduino 
	'''
	def connect(self):
		# take an object from serial library
                arduino = serial.Serial(self.port, self.speed)
		# delay to give the serial some time to initalize
		time.sleep = 2
		# get the final - clean path
		final_path = self.clean_path(self.path)
		# write the data
		arduino.write(final_path)
		# close
		arduino.close()
