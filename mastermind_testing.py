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

    return (ftime, guesses)


# for benchmarking tests using random as one test
# is not indicative of overall performance.
def average_test(code, colors, pegs):
    
    guesses = 0
    max_num = 0
    times = 0
    max_time = 0
    for i in range(100):
        (time, guess) = test(code, colors, pegs, 'random', False)
        guesses += guess
        times += time
        if guess > max_num:
            max_num = guess
        if time > max_time:
            max_time = time

    return (max_num, guesses / 100, max_time, time / 100)
    
    


def doallrand(colours, pegs):

    guesses = 0
    codes = 0
    max_num = 0
    max_t = 0
    time = 0
    for code in Mastermind(colours, pegs).codes():
        (m, guess, m_t, t) = average_test(code, colours, pegs)
        guesses += guess
        time += t
        if m > max_num:
            max_num = m
        if m_t > max_t:
            max_t = m_t
        codes += 1

    print("avg time: " + str(time/codes))
    print("max time: " + str(max_t))
    print("max num: " + str(max_num))
    print("avg num: " + str(guesses/codes))

    return


def doall(colours, pegs, strategy):
    guesses = 0
    codes = 0
    max_num = 0
    max_t = 0
    time = 0
    
    for code in Mastermind(colours, pegs).codes():
        (t, g) = test(code, colours, pegs, strategy, False)
        guesses += g
        time += t
        if g > max_num:
            max_num = g
        if t > max_t:
            max_t = t
        codes += 1

    print("avg time: " + str(time/codes))
    print("max time: " + str(max_t))
    print("max num: " + str(max_num))
    print("avg num: " + str(guesses/codes))
    
    return guesses


if __name__ == '__main__':

    print("Tests for Random Guess")
    print("----- 3,3")
    doallrand(3,3)
    print("----- 4,3")
    doallrand(4,3)
    print("----- 5,3")
    doallrand(5,3)
    print("----- 6,3")
    doallrand(6,3)
    print("----- 4,4")
    doallrand(4,4)
    print("----- 5,4")
    doallrand(5,4)
    print("----- 6,4")
    doallrand(6,4)

    print("\n")
    print("Tests for Donald Knuth's Five Guess Algorithm")
    print("----- 3,3")
    doall(3,3,'dk')
    print("----- 4,3")
    doall(4,3,'dk')
    print("----- 5,3")
    doall(5,3,'dk')
    print("----- 6,3")
    doall(6,3,'dk')
    print("----- 4,4")
    doall(4,4,'dk')
    print("----- 5,4")
    doall(5,4,'dk')
    print("----- 6,4")
    doall(6,4,'dk')

    print("\n")
    print("Tests for Donald Knuth’s Algorithm on Remaining Guesses")
    print("----- 3,3")
    doall(3,3,'dkr')
    print("----- 4,3")
    doall(4,3,'dkr')
    print("----- 5,3")
    doall(5,3,'dkr')
    print("----- 6,3")
    doall(6,3,'dkr')
    print("----- 4,4")
    doall(4,4,'dkr')
    print("----- 5,4")
    doall(5,4,'dkr')
    print("----- 6,4")
    doall(6,4,'dkr')
    
    
