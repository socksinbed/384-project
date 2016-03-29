import itertools



def init_guess_set():
    stuff = [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]
    S = itertools.product(*stuff)
    S2 = []
    for thing in S:
        S2.append(thing)

    return S2


def best_guess(S):

    most_removed = 0
    best = None
    for guess in S:
        num_eliminated = least_eliminated(S, guess)
        if num_eliminated >= most_removed:
            most_removed == num_eliminated
            best = guess

    return best
        

def least_eliminated(S, guess):

    possible_responses = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (4, 0)]
    least_removed = 1296
    for response in possible_responses:
        remove_count = count_not_matching(S, guess, response)
        if remove_count < least_removed:
            least_removed = remove_count
    
    return least_removed

def count_not_matching(S, guess, response):

    whites, blacks = response
    remove_count = 0
    for combo in S:
        if not check_blacks(guess, combo, blacks) or not check_whites(guess, combo, whites, blacks):
            remove_count += 1

    return remove_count


def remove_not_matching(S, guess, response):

    whites, blacks = response
    remove_count = 0
    S2 = list(S)
    for combo in S:
        if not check_blacks(guess, combo, blacks) or not check_whites(guess, combo, whites, blacks):
            S2.remove(combo)

    return S2
                      
def check_whites(previous_guess, new_guess, num_whites, num_blacks):

    pguess = list(previous_guess)
    nguess = list(new_guess)
    num_hits = 0

    for peg in pguess:
        if peg in nguess:
            num_hits += 1
            nguess.remove(peg)

    
    if num_hits == num_whites + num_blacks:
        return True

    else:
        return False

    
def check_blacks(previous_guess, new_guess, num_blacks):

    pguess = list(previous_guess)
    nguess = list(new_guess)
    num_hits = 0
    
    for i, peg in enumerate(pguess):
        if nguess[i] == peg:
            num_hits += 1
    
    if num_hits == num_blacks:

        return True

    else:
        return False
