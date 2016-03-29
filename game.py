import itertools
import collections
from mastermindtester import *


# Main loop for program execution.  Should run continuously until user enters
# "exit".
def main():
	S = init_guess_set()
	guess = [1,1,2,2] #initial guess
	i = 1
	print("Guess ", i, ": ", guess, "\n")

	while(1):

		white = input("Number of white pins: ")
		if white == "exit":
			print("Exiting...\n")
			return
		black = input("Number of black pins: ")
		if black == "exit":
			print("Exiting...\n")
			return
		print("\nChecking next move...")
		print("---------------------")

		if int(white) == 0 and int(black) == 4:
			print("Game over! Num guesses = ", i)
			return

		S = remove_not_matching(S, guess, (int(white), int(black)))
		guess = best_guess(S)
		i += 1
		print("Guess ", i, ": ", guess, "\n")


if __name__ == '__main__':
	main()