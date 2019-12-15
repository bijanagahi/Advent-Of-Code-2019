import re # reeeeeee
from itertools import permutations
from hashlib import md5

puzzle_input = '''<x=17, y=5, z=1>
<x=-2, y=-8, z=8>
<x=7, y=-6, z=14>
<x=1, y=-10, z=4>'''

# # Example input
puzzle_input = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''

# Harder example:
puzzle_input = '''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>'''

NUM_STEPS = 10000
states = set()

class Moon(object):
    """Moon Object"""
    def __init__(self, _input, _id):
        self.pos = self.parseInput(_input)
        self.vel = [0, 0, 0]
        self.trail = {}
        self.step = 0
        self.overlapped_steps = {}
        self.id = _id
        self.flag = False
        self.delta = 0
        self.isStable = False

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
        self.step+=1
        self.saveState()

    def saveState(self):
        # state = md5(str(self).encode()).hexdigest()
        state = str(self)
        if state in self.trail:
            # Mark which step we saw the same state
            self.trail[state].append(self.step)
            # self.overlapped_steps.append(self.step)
            self.overlapped_steps[self.step] = state # Maybe? #self.trail[state]
            if self.step-1 in self.overlapped_steps and self.step-2 in self.overlapped_steps:
                # We found the period.
                delta1 = self.step - self.overlapped_steps[self.step]
                delta2 = (self.step-1) - self.overlapped_steps[self.step-1]
                # delta3 = self.step -2 - self.overlapped_steps[self.step-2]
                # delta4 = self.step -3 - self.overlapped_steps[self.step-3]
                if delta1==delta2:
                    if not self.flag:
                        print(f"Moon #{self.id} has a period of {delta1}, starting at step {self.step-4}")
                        self.flag = True


            # new_delta = self.step - self.overlapped_steps[self.step]
            # if new_delta == self.delta:
            #     print(f"Moon #{self.id} has a period of {self.delta}")
            #     self.flag = True
            # else:
            #     self.delta = new_delta
            # if self.step-1 in self.overlapped_steps and self.step-2 in self.overlapped_steps and self.step-3 in self.overlapped_steps:
            #     if not self.flag:
            #         print(f"Moon #{self.id} has a period of {self.step-3}")
            #         self.flag = True

        else:
            # self.trail.add(state)
            self.trail[state] = [self.step]

    def __str__(self):
        return f"pos=<x= {self.pos[0]}, y= {self.pos[1]}, z= {self.pos[2]}>, vel=<x= {self.vel[0]}, y= {self.vel[1]}, z= {self.vel[2]}>"


def main():
    moons = []
    mid = 0
    for line in puzzle_input.splitlines():
        m = Moon(line,mid)
        m.saveState() # save the initial state
        moons.append(m)
        mid+=1
    print("\nInitial State (0 steps):")
    print('\n'.join([str(moon) for moon in moons]))
    num_found = 0
    while num_found < 4:
    # for step in range(1,927):
        # print(f"\nAfter {step} steps:")
        for x,y in permutations(moons, 2):
            x.calculateGravity(y)
        for moon in moons:
            moon.update()
        num_found = sum([moon.flag for moon in moons])

if __name__ == '__main__':
    main()
