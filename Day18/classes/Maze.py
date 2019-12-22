class Maze(object):
    """docstring for Maze"""
    def __init__(self, width, height):
        # self.grid = [[None for i in range(sizeX)] for j in range(sizeY)]
        self.grid = [None] * (width*height)
        self.width = width
        self.height = height

    def addNode(self, node):
        self.grid[self.c2i(node.x, node.y)] = node

    def i2c(self, i):
        x = i%self.width
        y = i//self.width
        return (x,y)

    def c2i(self,x,y):
        return x + self.width*y

    def __str__(self):
        # return '\n'.join([''.join([str(y) for y in x]) for x in self.grid])
        r = ''
        for i in range(len(self.grid)):
            if i%self.width == 0:
                r+=f'\n{str(self.grid[i])}'
            else:
                r+=str(self.grid[i])
        return r