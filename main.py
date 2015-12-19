'''
' Main just connect all files together
'''
# import maze , pyserial time and files
import Tkinter as tk
import cPickle, copy
import serial, time
import maze, arduino_connection

# main function
def main():
        # start point
	init = [5, 12]
	# end point
	goal = [10, 55]
	# cost
	cost = 5
	# require the maze grid
	grid = cPickle.load(open('save.p', 'rb'))
        # object from maze class and perform search
	playground = maze.maze(grid, init, goal, cost)
	path = playground.search()
        # entering the port
	port = "/dev/ttyUSB0"
	# sending data
	ard = arduino_connection.arduino_connection(path, port)
	# start serial connection
	ard.connect()
        
if __name__ == "__main__":
	main()



