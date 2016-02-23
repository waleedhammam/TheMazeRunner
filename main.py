import Tkinter as tk
import cPickle, copy
import serial, time
from maze import maze
from arduino_connection import arduino_connection

def main():
    init = [28, 28]
    goal = [53, 4]
    cost = 5
    
    # ratio = robot_diameter / ( 2* maze_cell_long)
    # it's initially = 1 but you can edit it according your robot design
    ratio = 1
    #save.p is the maze pickle file , replace it with your maze file (it should be in the same format)
    simple_grid = cPickle.load(open('save.p', 'rb'))

    maze_obj = maze(simple_grid, init, goal,cost,ratio)

    grid_row_no = len(simple_grid)
    grid_col_no = len(simple_grid[0])
    total_barrier = set()

    for row in range(grid_row_no) :
        for col in range(grid_col_no):
            cur_node = simple_grid[row][col]
            if  cur_node == 1 :
                node_barrier = maze_obj.update_b(row, col)
                total_barrier.update(node_barrier) 

    maze_obj.set_grid(total_barrier)

    path1 = maze_obj.search()
    #print str(path) + "  len = " + str(len(path))
    print str(path1) + "  len = " + str(len(path1))
    port = "/dev/ttyACM1"

    ard = arduino_connection(path1, port)
    new_path = ard.shut_your_mouth()
    print str(new_path) + "  len = " + str(len(new_path))


    '''
    ard.connect()
    '''


if __name__ == "__main__":
    main()
