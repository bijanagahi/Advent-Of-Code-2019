import sys
from classes.Node import Node
from classes.Maze import Maze

# Day 18 Solution by Bijan Agahi and Josh Lund #

def parse(f):
  grid = []
  for line in f.readlines():
    if '@' in line:
        entrance = (line.find('@'),len(grid))
    grid.append([char for char in line.strip()])
  return (grid, entrance)
       

# def parseInput(puzzle_input):
#     maze = []
#     entrance = None
#     for line in puzzle_input.split():
#        if '@' in line:
#          entrance = (len(maze),line.find('@'))
#        maze.append([x for x in line])
#     return maze,entrance


def main(parsed_input):
    # print('\n'.join([''.join([y for y in x]) for x in grid]))
    grid, entrance = parsed_input
    print(entrance)
    sizeX = len(grid[0])
    sizeY = len(grid)
    print(f"Width: {sizeX}, Height: {sizeY}")
    maze = Maze(sizeX, sizeY)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            n = Node(x,y,grid[y][x])
            maze.addNode(n)
    print(maze)   
    # print(grid[1][1])
    # bfs(grid,(1,1))
    # print('\n'.join([''.join([y for y in x]) for x in grid]))
    maze.bfs(entrance)
    print([str(x) for x in maze.keys])


if __name__ == '__main__':
    main(parse(open(sys.argv[1], 'r')))