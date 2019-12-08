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
	inc = int(guess[0])
	flag = False
	for char in guess[1:]:
		if (prev == char) and not flag:
			flag = True

		if inc > int(char):
			return False

		prev = char
		inc = int(char)
	return flag




for guess in range(range_low,range_high):
	# Validate the guess
	if not validateGuess(guess):
		continue
	# If we got here it's a valid password
	valid_passwords += 1

print(valid_passwords)

