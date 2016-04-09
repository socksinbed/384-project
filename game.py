import time
from mastermind import *
            
# Main loop for program execution.  Should run continuously until user enters
# "exit".
def main():
    
        num_colors = input("Welcome to Mastermind! How many colours are we playing with? (Between 2 and 9) ")
        num_pegs = input("\nAnd how many pegs? (Between 2 and 4) ")

        use_starting_library = input("\nShould we use an 'opening book'? \n" +
                                     "It consults a saved table containing the optimal \nfirst guesses for given sizes of mastermind games.\n" +
                                     "Significantly reduces processing time as\nthe first guess takes the longest time.\n" +
                                     "Type y for yes and n for no. ")

        strategy = input("Which strategy should the guesser use? Type a number.\n    1. Guess that eliminates most possibilities, including guesses that couldn't be the right answer.\n    2. Guess that eliminates most possibilites, excluding non-candidates.\n    3. Random choice from possible candidates.")

        show_time = input("\nDo you want to see the processing time for EACH guess? ")

        if show_time == 'y':
            show_time = True
    
        print("Thank you!")
        
        game = Mastermind(int(num_colors), int(num_pegs))

        if strategy == '1':
            guess_fn = game.best_guess
        elif strategy == '2':
            guess_fn = game.best_guess_from_remaining
        else:
            guess_fn = game.random_guess
        
        i = 1
        ttime = 0

        while(1):
            print("\nChecking next move...")
            print("---------------------")
            
            if i == 1 and use_starting_library == 'y':
                guess = first_guess(int(num_colors), int(num_pegs))
            else:
                stime = time.process_time()
                guess = guess_fn()
                gtime = time.process_time() - stime
                ttime += gtime
                
            print("Guess ", i, ": ", guess, "\n")

            
            if show_time and (i != 1 or not use_starting_library == 'y'):
                print("Time taken: {} seconds".format(gtime))
                
            white = input("Number of white pins: ")
            if white == "exit":
                print("Exiting...\n")
                return

            black = input("Number of black pins: ")
            if black == "exit":
                print("Exiting...\n")
                return



            if int(white) == 0 and int(black) == int(num_pegs):
                print("Game over! Number of guesses = ", i)
                print("Time used: {} seconds".format(ttime))
                return

            game.eliminate(guess, (int(white), int(black)))
            i += 1


if __name__ == '__main__':
	main()
