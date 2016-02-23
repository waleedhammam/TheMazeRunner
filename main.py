import Tkinter as tk
import cPickle, copy
import serial, time
from maze import maze
from arduino_connection import arduino_connection
'''
def update_b(row, col, ratio) :
    cur_node = (row, col)

    barrier = set()

    for i in range(ratio) :
        new_nodes  = []
        up_node  = (row + i, col)
        down_node  = (row - i,col)
        left_node = (row ,col - i)
        right_node =  (row ,col + i)
        basic_nodes = [up_node, down_node, left_node, right_node]
        new_nodes.extend(basic_nodes)
        for j in range(ratio ):
            #left up
            left_up_node = (row - i, col - j)
            #right up
            right_up_node = (row - i, col + j)
            #left down
            left_down_node = (row + i, col - j)
            #right down
            right_down_node = (row + i, col + j)
            corner_nodes = [left_up_node, left_down_node, right_up_node, right_down_node]
            new_nodes.extend(corner_nodes)

        barrier.update(set(new_nodes))
        return barrier


def make_new_robotic_grid(old_grid, row_no, col_no, brarrier):
    new_grid = []
    brarrier_list = list(brarrier)
    for row in range(row_no):
        new_grid.append([])
        for col in range(col_no):
            #print row, col
            if (row,col) in brarrier_list :
                new_grid[row].append(1)
            else :
                new_grid[row].append(0)
    return new_grid

#shortens the path 
def shut_your_mouth(dirty_path):
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
'''
def main():
    init = [28, 28]
    goal = [53, 4]
    cost = 5

    ratio = 3
    #maze(self, grid, init, goal, cost, robot_ratio)

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
    #print path


if __name__ == "__main__":
    main()
