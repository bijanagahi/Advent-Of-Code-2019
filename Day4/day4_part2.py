# https://adventofcode.com/2019/day/4
# --- Day 4: Secure Container ---
#
# Authors: Bijan Agahi

range_low = 347312
range_high = 805915

valid_passwords = 0

def validateGuess(guess):
	if not len(set(str(guess))) < 6:
		return False
	guess = str(guess)
	prev = guess[0]
	repeat_count = 1
	for char in guess[1:]:
		# Check if we hit a double and nothing more
		if (char != prev) and repeat_count == 2:
			return True
		if char == prev:
			repeat_count += 1
		else:
			repeat_count = 1
		prev = char
	if repeat_count == 2:
		return True
	return False

def checkIncreasing(guess):
	guess = str(guess)
	inc = int(guess[0])
	for char in guess[1:]:
		if inc > int(char):
			return False
		inc = int(char)
	return True





for guess in range(range_low,range_high):
	# Validate the guess
	if not validateGuess(guess):
		continue
	if not checkIncreasing(guess):
		continue
	# If we got here it's a valid password
	valid_passwords += 1

print(valid_passwords)

