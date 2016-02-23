''''''''''''''''''''''''''''''''''''''''''
' Main function where the program starts '
''''''''''''''''''''''''''''''''''''''''''

# Importing Required Libraries and classes
import Tkinter as tk
import cPickle, copy
import serial, time
from maze import maze
from arduino_connection import arduino_connection

# Main
def main():
    # initial Point
    init = [28, 28]
    # Final point
    goal = [53, 4]
    # Move Cost
    cost = 1
    # Connection Speed
    speed = 115200
    # Barriers ratio to path width = robot_diameter / (2 * maze cell long)
    ratio = 1    
    # save.p is the maze pickle file, and generates the maze
    grid = cPickle.load(open('save.p', 'rb'))
    # Serial Port
    port = "/dev/ttyACM1"
    # Taking an object from maze class
    maze_obj = maze(grid, init, goal,cost,ratio)

    '''''''''''''''''''''''''''''''''''''''''
    ' Building the final maze with Barriers '              
    '''''''''''''''''''''''''''''''''''''''''
    grid_row_no,  grid_col_no = len(grid), len(grid[0])
    total_barrier = set()
    for row in range(grid_row_no) :
        for col in range(grid_col_no):
            cur_node = grid[row][col]
            if  cur_node == 1 :
                node_barrier = maze_obj.update_b(row, col)
                total_barrier.update(node_barrier) 
    maze_obj.set_grid(total_barrier)

    # Performing search
    path = maze_obj.search()
    # Taking an object from arduino_connection class
    ard_obj = arduino_connection(path, port, speed)
    # Sending Data to arduino
    ard_obj.connect()

'''''''''''''''''
' Starting main '
'''''''''''''''''
if __name__ == "__main__":
    main()
