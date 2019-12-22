from classes.Node import Node
import random

class Maze(object):
    """Maze class. Holds a 1D array reperesenting the maze"""
    def __init__(self, width, height):
        self.grid = [None] * (width*height)
        self.width = width
        self.height = height
        self.deltas = [(1,0),(-1,0),(0,1),(0,-1)]
        self.nodes = {}
        self.keys = []
        self.doors = []

    def addNode(self, node):
        self.grid[self.c2i(node.x, node.y)] = node
        self.nodes[(node.x,node.y)] = node

    # Convert 1D index to 2D coordinate
    def i2c(self, i):
        x = i%self.width
        y = i//self.width
        return (x,y)

    # Convert 2D coordinate to 1D index
    def c2i(self,x,y):
        return x + self.width*y

    def bfs(self, start):
        assert isinstance(start, tuple), "BFS requires a tuple as a starting coordinate"
        start = self.nodes[start]
        stack = [start]
        self.markVisited(start)
        while(stack):
            self.addToStack(stack, stack.pop())

    def addToStack(self,stack,node):
        random.shuffle(self.deltas) # for funzies
        for delta in self.deltas:
             if (node.x + delta[0], node.y + delta[1]) in self.nodes:
                newNode = self.nodes[(node.x + delta[0], node.y + delta[1])]
                if self.legalNode(newNode):
                    stack.append(newNode)
                    self.markVisited(newNode)

    
    def legalNode(self, node):
        # If it's a wall, it's not a legal node.
        if node.type == "WALL" or node.visited:
            return False
        # Paths are fine
        if node.type == 'PATH':
            return True
        # Here's the interesting one, doors. We need to see if we have the key first
        if node.type == 'DOOR':
            if node.value.lower() in self.keys:
                return True
            else:
                return False
        return True


    
    def markVisited(self, node):
        if node.type == 'KEY':
            self.keys.append(node.value)
        if node.type == 'DOOR':
            return self.doors.append(node.value)
        node.visited = True

    def __str__(self):
        r = ''
        for i in range(len(self.grid)):
            if i%self.width == 0:
                r+=f'\n{str(self.grid[i])}'
            else:
                r+=str(self.grid[i])
        return r