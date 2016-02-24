#The Maze Runner
AI Class Project that designed to solve any maze and send the path of the goal point to a robot via arduino.

###Code Design 
This project consists of 2 classes and a main file.
First Class (maze) contains functions that solve the maze and produces a suitable form of the robot's path
Second Class (arduino_connection) is responsible for transimiting the robot's path to an arduino.
And of course (Main) file connects all these staff together, It's the machine that connects all program's parts together
to make it work !

###Search Algorithm 
"A-Star" algorithm it's a world wide used algorithm that returns the optimal path to the goal.
Check: https://en.wikipedia.org/wiki/A*_search_algorithm

###Code Rules
The robot's size must not exceed the maze's width.
The maze should have at least one solution.

###Software Requirments
Pyserial library. Download link: https://pypi.python.org/pypi/pyserial/2.7
Python 2.x .      Download link: https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tar.xz
