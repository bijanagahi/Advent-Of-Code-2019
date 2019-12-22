class Node(object):
    """docstring for Node"""
    def __init__(self, posX, posY, value):
       self.x = posX
       self.y = posY
       self.value = value
       self.type = self.setType(self.value)
       self.visited = False # Have we seen this node before? (for BFS)

    def setType(self, value):
       # Take care of the non-letter chars
       if value == '#':
         return 'WALL'
       if value == '.':
         return 'PATH'
       if value == '@':
         return 'PATH'
       # Take care of the keys/doors
       if value.isupper():
         return 'DOOR'
       if value.islower():
         return 'KEY'
       # At this point it's got to have returned something
       raise TypeError("Could not parse block type")

    def __str__(self):
        return self.value