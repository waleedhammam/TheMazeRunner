''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' arduino_connection Class is the link between Python and Arduino.     '
' shut_your_mouth and clean_path function converts the path into       '
' another form that is easy to deal with on arduino                    '
' Connect function takes that path and sends it via serial port to     '
' the arduino device                                                   '
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# importing pyserial library, and time library will be used for sleep
import serial, time

class arduino_connection(object):
	'''''''''''''''''''''''''''''''''''''''''''''''''''
	' The main constructor that takes 3 parameters    '
	' path -> Path generated from search              '
	' port -> Serial Port position                    '
	' speed -> Serial's transfer speed                '
	'''''''''''''''''''''''''''''''''''''''''''''''''''
	def __init__(self, path, port, speed):
		self.path = path
		self.port = port
		self.speed = speed
	
	'''''''''''''''''''''''''''''''''''''''''''''''''''
	' shut_your_mouth function Optomizes the robot's  '
	' path by reducing the points in x-dir            '
	' e.x : it reduces points from 274 to 74          '
	' so arduino can handle them                      '
	'''''''''''''''''''''''''''''''''''''''''''''''''''
	def shut_your_mouth(self):
		dirty_path = self.path
		clean_path = []
		cur_node = dirty_path[0]
		clean_path.append(cur_node)
		for i in range (1, len(dirty_path) ):
			next_node = dirty_path[i]
			if next_node[0] != cur_node [0] :
				prev_node = dirty_path[i-1]
				#print prev_node, "next", next_node
				if prev_node not in clean_path : clean_path.append(prev_node)
				if next_node not in clean_path : clean_path.append(next_node)
				cur_node = next_node
				if dirty_path[-1]    not in clean_path : clean_path.append(dirty_path[-1])
				#new_clean_path = list(set(clean_path))
		return clean_path

	''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	' clean_path function takes the reduced path and       '
	' eliminates the brackets and parantesess to make      '
	' it easy for arduino to read points                   '
	' return value is the final path and ready to be sent  '
	''''''''''''''''''''''''''''''''''''''''''''''''''''''''
	def clean_path(self):
	    path = self.shut_your_mouth()
		# convert the list to string
	    path_to_ard = str(path)
	    # iterate over the list to eliminate brackets and parantesess
	    for i in ["[","]","("," "] :
	        path_to_ard = path_to_ard.replace(i,"")
	    path_to_ard = path_to_ard.replace("),", ",")
	    path_to_ard = path_to_ard.replace(")", "")
	    # adding a * and $ symbol to let arduino know the start and end of receive
	    path_to_ard = "*" + path_to_ard + "$"
	    return path_to_ard

	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	' connect function initiates a connection to arduino '
	' via serial ports and send the final path           '
	''''''''''''''''''''''''''''''''''''''''''''''''''''''
	def connect(self):
		# get the final - clean path
		final_path = self.clean_path()
		# Printing final path
		print "Final Path is: "
		print final_path
		# Trying to make connection to arduino
		print "Connecting ..."
		try:
			# take an object from serial library
			arduino = serial.Serial(self.port, self.speed)
			# delay to give the serial some time to initalize
			time.sleep = 2
			# write the data
			arduino.write(final_path)
			# Connection completed
			print "Success, Data sent"
			# close
			arduino.close()
		except serial.SerialException:
			print "it was an error and now it's an exception :D"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' End of class , Don't forget to import it in your application      '
' you may use from arduino_connection import arduino_connection     '
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
		