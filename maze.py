'''
' Hello, This class is a maze solver using a- star algorithm and a heuristic function 
' to solve a very difficult maze :D, 
' to use this class just take an object in your main program file
' this class is open source, feel free to make your commits and send us your feedback.
'''
class maze(object):
	'''
	' __init__ method works as a constructor, takes 5 parameters,
	' self -> essential for python
	' grid -> the maze you want to solve
	' init -> the start point as a list
	' goal -> the final point as a list
	' cost -> the move cost
	'''
	def __init__(self, grid, init, goal, cost):
		self.grid = grid
		self.init = init
		self.goal = goal
		self.cost = cost
		# the actions you are allowd to
		self.delta = delta = [ [-1,  0 ], # go up    -previous row, same column
			           [ 0, -1 ], # go left  -same row    , previous column
			           [ 1,  0 ], # go down  -next row    , same column
			           [ 0,  1 ]] # go right -same row    , next column
		# rows_no, cols_no , will be used to initialize closed list
		self.rows_no = len(grid)
		self.cols_no = len(grid[0])
		# initializing closed list, [the points you visited]
		self.closed = [ [0 for row in range(self.cols_no)] for col in range(self.rows_no )]
		# initializing first item(start point with 1)
		self.closed[init[0]][init[1]] = 1
	'''
	' heuristic function is a helper function makes an indicator for reaching the goal
	' logically it drives the distance from current point to gaol discarding obstacles
	' function heuristic takes one parameter node as a list, consisits of x and y co-ord
	' and return the sum of'em (the diaognal distance)
	'''
	def heuristic(self, node):
		# x- distance from current point to goal
		dx = abs(node[0] - self.goal[0])
		# y- distance from current point to goal
		dy = abs(node[1] - self.goal[1])
		return dx + dy
	'''
	' search function is an a* algorithm, it solves the maze,
	' if there's is an optimal way it returns it
	' otherwise returns fail
	'''
	def search(self):
		# starting position
	    x, y = self.init[0], self.init[1]
	    # current path (just initalizing)
	    path = [(x, y)]
	    # initializing g with 0 and get current heuristic
	    g = 0
	    h = self.heuristic([x, y])
	    # calcualting f function which function will calc path according it
	    f = g + h
	    # intitalizing an open list to put visited points in it
	    open = [[f, g, (x, y), path]]   
	    # just two variables, if goal found, or no path at all
	    found, resign = False, False
	    # iterating over the whoooole path
	    while not found and not resign:
	    	# if there's no points to visit then no path and return fail
	        if len(open) == 0:
	            resign = True
	            return "Sorry, Unable to find path .."
	        # else continue looping     
	        else:
                        # sort and reverse open list
	            open.sort(reverse = True)
	            # making a next for the next node
	            next = open.pop()  
	            # getting g
	            g = next[1]
	            # getting x and y
	            x, y = next[2][0], next[2][1]
	            # getting x and y
	            path = next[3]
	            # if we reached our goal then return the path
	            if x == self.goal[0] and y == self.goal[1]:
	                found = True
	                return path 
	            else:
	            	# else continue iterating with the actions in delta
	                moves_no = len(self.delta)
	                for i in range(moves_no):
	                	# calcualting new x and y according to delta
	                    x2 , y2= x + self.delta[i][0], y + self.delta[i][1]
	                  	# put limits of the grid to prevent getting out
	                    if x2 >= 0 and x2 < len(self.grid) and y2 >=0 and y2 < len(self.grid[0]):
	                    	# Checking if the point is not visited before
	                        if self.closed[x2][y2] == 0 and self.grid[x2][y2] == 0:
	                        	# calculating new path
	                            path2 = path + [(x2, y2)]
	                            # calculating new g    
	                            g2 = g + self.cost
	                            # calculating new h
	                            h2 = self.heuristic([x2, y2])
	                            # calculating new f   
	                            f2 = g2 + h2
	                            # appending this path to the old one       
	                            open.append([f2, g2, (x2, y2), path2]) 
	                            # close the visited point    
	                            self.closed[x2][y2] = 1
