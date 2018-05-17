"""
Determines the solution to a maze problem.
Uses a gid to represent the maze.
This grid is input from a text file.
Uses a stack-based backtracking algorithm.

Replace any "<your code>" comments with your own code statement(s)
to accomplish the specified task.
Do not change any other code.

The following files must be in the same folder:
  abstractcollection.py
  abstractstack.py
  arrays.py
  arraystack.py
  grid.py
"""

from arraystack import ArrayStack
from grid import Grid

BARRIER = '-'  # barrier
FINISH = 'F'   # finish (goal)
OPEN = 'O'     # open step
START = 'S'    # start step
VISITED = '#'  # visited step

def main():
    maze = getMaze()
    print("The maze:")
    printMaze(maze)
    (startRow, startCol) = findStartPosition(maze)
    if (startRow, startCol) == (-1, -1):
        print("This maze does not have a start symbol.")
        return
    success = solveMaze(startRow, startCol, maze)
    if success:
        print("Maze solved:")
        printMaze(maze)
    else:
        print("There is no solution for this maze.")
    
def getMaze():
    """Reads the maze from a text file and returns a grid that represents it."""
    name = input("Enter a file name for the maze: ")
    fileObj = open(name, 'r')
    firstLine = list(map(int, fileObj.readline().strip().split()))
    rows = firstLine[0]
    columns = firstLine[1]
    maze = Grid(rows, columns)
    for row in range(rows):
        line = fileObj.readline().strip()
        column = 0
        for character in line:
            maze[row][column] = character
            column += 1
    return maze

# Returns a tuple containing the row and column position of the start symbol.
# If there is no start symbol, returns the tuple (-1, -1)
def findStartPosition(maze):
#   Part 1:
    for row in range(maze.getHeight()):
        for column in range(maze.getWidth()):
            if maze[row][column] == START:
                return (row,column)
            else:
                return(-1, -1)
                    
# Prints the maze with no spaces between cells.
def printMaze(maze):
#   Part 2:
    result = ""
    for row in range(maze.getHeight()):
        for column in range(maze.getWidth()):
            result+= str(maze._data[row][column])
    return result

# (row,column) is the position of the start symbol in the maze.
# Returns True if the maze can be solved or False otherwise.
def solveMaze(row, column, maze):
    # States are tuples of coordinates of cells in the grid.
    stack = ArrayStack()
    stack.push((row, column))
    while not stack.isEmpty():
        (row, column) = stack.pop()
        if  maze[row][column] == FINISH: 
            return True
        if maze[row][column] == VISITED:
            continue

        # Cell has not been visited.
        # Mark it as visited.
        maze[row][column] = VISITED
        
        # Push adjacent unvisited positions onto the stack:
        # Part 3:
        for row, column in [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]:
            if maze[row][column] != BARRIER or VISITED:
                stack.push((row, column))
    return False

main()
