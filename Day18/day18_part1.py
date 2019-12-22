import sys
from classes.Node import Node
from classes.Maze import Maze

def bfs(grid, pt):
  stack = [pt]
  while(stack):
    addToStack(grid, stack, stack.pop())

deltas = [(1,0),(-1,0),(0,1),(0,-1)]
def addToStack(grid, stack, pt):
  for delta in deltas:
    newPt = addPts(pt, delta)
    if inBounds(grid, newPt) and legalChar(grid, newPt):
      stack.append(newPt)
      markVisited(grid, newPt)

def addPts(pt1, pt2):
  return (pt1[0] + pt2[0], pt1[1] + pt2[1])

def inBounds(grid, pt):
  return (0 <= pt[0] < len(grid)) and (0 <= pt[1] < len(grid[0]))

def legalChar(grid, pt):
  return grid[pt[0]][pt[1]] != "#"

def markVisited(grid, pt):
  grid[pt[0]][pt[1]] = "#"

def parse(f):
  grid = []
  for line in f.readlines():
    grid.append([char for char in line.strip()])
  return grid
       

# def parseInput(puzzle_input):
#     maze = []
#     entrance = None
#     for line in puzzle_input.split():
#        if '@' in line:
#          entrance = (len(maze),line.find('@'))
#        maze.append([x for x in line])
#     return maze,entrance


def main(grid):
	print('\n'.join([''.join([y for y in x]) for x in grid]))
	sizeX = len(grid[0])
	sizeY = len(grid)
	print(f"Width: {sizeX}, Height: {sizeY}")
	maze = Maze(sizeX, sizeY)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			n = Node(j,i,grid[i][j])
			maze.addNode(n)
	print(maze)
	i = maze.c2i(0,2)
	print(i,maze.grid[i])	
    # bfs(grid,(1,1))
    # print(grid)



if __name__ == '__main__':
    main(parse(open(sys.argv[1], 'r')))