from mastermind import *
import time


def get_blacks(code, guess):

    blacks = 0
    for i, x in enumerate(code):
        if guess[i] == x:
            blacks += 1

    return blacks


#actual whites = get_whites - get_blacks
def get_whites(code, guess):

    whites = 0

    lguess = list(guess) #make list so can remove
    for x in code:
        if x in lguess:
            lguess.remove(x)
            whites += 1

    return whites

def test(code, colors, pegs, strategy, printing=True):

    m = Mastermind(colors, pegs)
    initial_guess = None

    if colors > 9 or colors < 2:
        print("Invalid number of colors. Choose between (2-9)")
        return

    if pegs > 4 or pegs < 2:
        print("Invalid number of pegs. Choose between (2-4)")
        return

    if pow(colors, pegs) > 1296:
        print("Warning! Very large search space!\nThis may timeout or take an extremely long time.")
    
    if strategy == 'dk': # donald knuth 5 guess algorithm
        guesser = m.best_guess
        initial_guess = first_guess(colors, pegs)
        
    elif strategy == 'dkr': # donald knuth on only remaining
        guesser = m.best_guess_from_remaining
        initial_guess = first_guess(colors, pegs)

    elif strategy == 'minimax': # min maxes, no first guess, same as dk
        guesser = m.best_guess

    elif strategy == 'mmr': # min max with only remaining guesses
        guesser = m.best_guess_from_remaining

    elif strategy == 'random': # random guesses from remaining
        guesser = m.random_guess

    else:
        print("Invalid strategy")
        return

    guesses = 0
    blacks = 0
    whites = 0

    stime = time.process_time()
    while blacks != pegs:

        
        if guesses == 0 and initial_guess:
            next_guess = initial_guess
        else:
            next_guess = guesser()
        whites = get_whites(code, next_guess)
        blacks = get_blacks(code, next_guess)
        guesses += 1

        m.eliminate(next_guess, (whites - blacks, blacks))


    ftime = time.process_time() - stime
    if printing:
        print("Time taken {} colors, {} pegs, code: {}: {} seconds".format(colors, pegs, code, ftime))
        print("Guesses taken: {}".format(guesses))

    return guesses


# for benchmarking tests using random as one test
# is not indicative of overall performance.
def average_test(code, colors, pegs):
    
    guesses = 0
    for i in range(100):
        guesses += test(code, colors, pegs, 'random', False)

    return guesses / 100
    
    


def doall():

    guesses = 0

    codes = 0
    for code in Mastermind(4, 2).codes():
        guesses += average_test(code, 4, 2)
        codes += 1


    return guesses/codes
