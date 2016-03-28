import itertools
import collections


# Main loop for program execution.  Should run continuously until user enters
# "exit".
def main():
	while(1):
		print(solve(0, 0), "\n")
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


# CSP/Heuristic search for Mastermind.
def solve(white, black):
	guess = [0] * 4
	return guess


if __name__ == '__main__':
	main()