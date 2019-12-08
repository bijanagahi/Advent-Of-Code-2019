# https://adventofcode.com/2019/day/2
# --- Day 2: 1202 Program Alarm ---
#
# Author: Bijan Agahi

program = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,6,23,27,1,5,27,31,1,10,31,35,2,10,35,39,1,39,5,43,2,43,6,47,2,9,47,51,1,51,5,55,1,5,55,59,2,10,59,63,1,5,63,67,1,67,10,71,2,6,71,75,2,6,75,79,1,5,79,83,2,6,83,87,2,13,87,91,1,91,6,95,2,13,95,99,1,99,5,103,2,103,10,107,1,9,107,111,1,111,6,115,1,115,2,119,1,119,10,0,99,2,14,0,0"
target = 19690720
# Opcode:		1
# Operation:	Addition
# Parameters:	3 (read_location1, read_location2, write_location3)

# Opcode:		2
# Operation:	Multiply
# Parameters:	3 (read_location1, read_location2, write_location3)

def parseOpcode(opcode, memory, pc):
	# Here we will handle opcode logic
	if opcode in [1,2]: # Addition / Multiplication
		read_from1 = memory[pc+1]
		read_from2 = memory[pc+2]
		write_to = memory[pc+3]
		if opcode == 1:
			memory[write_to] = memory[read_from1] + memory[read_from2]
		else:
			memory[write_to] = memory[read_from1] * memory[read_from2]

def main():
	flag = False
	noun = 0
	verb = 0

	for noun in range(100):
		for verb in range(100):
			# Reset the computer
			memory = [int(x) for x in program.split(',')]
			pc = 0 # Program counter, starts at location 0
			# Step 0: Set the noun and verb
			memory[1] = noun
			memory[2] = verb

			while pc < len(memory):
				# Step 1: Read the opcode
				opcode = memory[pc]
				# If the opcode is 99, end the program and dump memory
				if opcode == 99:
					# Check if we got the right answer 
					if memory[0] == target:
						print(memory)
						print(f"Target Found! Noun: {noun} | Verb: {verb}...answer = {100*noun+verb}")
						exit()
					else:
						break
				# Step 2: Parse the opcode and run the appropriate function
				parseOpcode(opcode, memory, pc)
				pc += 4 # increment the program counter to the next opcode.

if __name__ == '__main__':
	main()