import re # reeeeeee
from itertools import permutations
# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt

puzzle_input = '''<x=17, y=5, z=1>
<x=-2, y=-8, z=8>
<x=7, y=-6, z=14>
<x=1, y=-10, z=4>'''

# Example input
puzzle_input = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

# # # Harder example:
# puzzle_input = '''<x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>'''

NUM_STEPS = 50
KEY_STEPS = [1,11, 231,693,924, 2772]
# KEY_STEPS = [983,2351]

class Moon(object):
    """Moon Object"""
    def __init__(self, _input, mid):
        self.pos = self.parseInput(_input)
        self.initial_pos = [x for x in self.pos] # copy no ref
        self.vel = [0, 0, 0]
        self.id = mid
        self.step = 0

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
        self.step+=1
        self.pos = [sum(x) for x in zip(self.pos, self.vel)]
        # if self.pos == self.initial_pos and self.isStill():
        #     print(f"\n[{self.id}] is static at it's original position at step {self.step}\n{str(self)}")

    def calculateEnergy(self):
        return sum([abs(x) for x in self.pos]) * sum([abs(x) for x in self.vel])

    def isStill(self):
        return sum( [abs(x) for x in self.vel ] ) == 0

    def absVel(self):
        return [abs(x) for x in self.vel]

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
        if step in KEY_STEPS:
            print(f"\nKey Step ({step} steps):")
            all_vel = [sum(x) for x in zip(moons[0].absVel(),moons[1].absVel(),moons[2].absVel(),moons[3].absVel())]
            print(f"System velocity: {all_vel}")
            print('\n'.join([str(moon) for moon in moons]))
    # all_vel = [sum(x) for x in zip(moons[0].absVel(),moons[1].absVel(),moons[2].absVel(),moons[3].absVel())]
    # if 0 in all_vel:
    #     print(f"***\nStep {step} has a 0 velocity ({all_vel})")
    #     print('\n'.join([str(moon) for moon in moons]))
    #     print()
        # print('\n'.join([str(moon) for moon in moons]))
    print(f"\nFinal State ({NUM_STEPS} steps):")
    print('\n'.join([str(moon) for moon in moons]))

    # Calculate total energy
    print(f"Total Energy: {sum([moon.calculateEnergy() for moon in moons])}")


if __name__ == '__main__':
    main()
