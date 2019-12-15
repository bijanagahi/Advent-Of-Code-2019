import re # reeeeeee
from itertools import permutations

puzzle_input = '''<x=17, y=5, z=1>
<x=-2, y=-8, z=8>
<x=7, y=-6, z=14>
<x=1, y=-10, z=4>'''

# Example input
puzzle_input = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

# Harder example:
# puzzle_input = '''<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>'''

NUM_STEPS = 1000

class Moon(object):
    """Moon Object"""
    def __init__(self, _input, mid):
        self.pos = self.parseInput(_input)
        self.vel = [0, 0, 0]
        self.id = mid

    def parseInput(self, i):
        matches = re.findall(r"(-?\d{1,})",i)
        if not len(matches) == 3:
            raise IndexError("Regex match fail")
        return [int(p) for p in matches]

    def calculateGravity(self, adj):
        for index, val in enumerate(adj.pos):
            if self.pos[index] == val:
                continue
            self.vel[index] += 1 if self.pos[index] < val else -1

    def update(self):
        self.pos = [sum(x) for x in zip(self.pos, self.vel)]

    def calculateEnergy(self):
        return sum([abs(x) for x in self.pos]) * sum([abs(x) for x in self.vel])

    def __str__(self):
        return f"[{self.id}]: pos=<x= {self.pos[0]}, y= {self.pos[1]}, z= {self.pos[2]}>, vel=<x= {self.vel[0]}, y= {self.vel[1]}, z= {self.vel[2]}>"


def main():
    moons = []
    mid = 0
    for line in puzzle_input.splitlines():
        m = Moon(line,mid)
        moons.append(m)
        mid+=1
    print("\nInitial State (0 steps):")
    print('\n'.join([str(moon) for moon in moons]))
    
    for step in range(1,NUM_STEPS+1):
        # print(f"\nAfter {step} steps:")
        for x,y in permutations(moons, 2):
            x.calculateGravity(y)
        for moon in moons:
            moon.update()
        # print('\n'.join([str(moon) for moon in moons]))
    print(f"\nFinal State ({NUM_STEPS} steps):")
    print('\n'.join([str(moon) for moon in moons]))

    # Calculate total energy
    print(f"Total Energy: {sum([moon.calculateEnergy() for moon in moons])}")


if __name__ == '__main__':
    main()
