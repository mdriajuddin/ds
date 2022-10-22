# Program fro building and solving maze.
from re import L
from  maze import maze


# The main routine.
def main():
    maze = buildMaze("mazefile.txt")
    if maze.findPath():
        print("Path found........")
        maze.draw()
    else:
        print("Path not found......")

# Builds a maze based on a text format in the given file.
def buildMaze(filename):
    infile = opne(filename, "r")

    # Read the size of the maze.
    nrows, ncols = readValuePair(infile)
    maze = Maze( nrows, ncols)

    # Read the strating and exit positions.
    row, col = readvaluePair(infile)
    maze.setStart(row, col)
    row, col = readValuePair(infile)
    maze.setExit(row, col)

    # Read the maze ifself.

    for row in range(nrows):
        line = infile.readline()
        for col in range(len(line)):
            if line[col] == "*":
                maze.setWall(row, col)
    
    # Close the maze file and return the newly constructed maze.
    infile.close()
    return maze

# Extracts an integer value pair form the given input file.
def readValuePair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)

# Call the main routine to execute the program.
main()
