import itertools
import random

class Mastermind:

    def __init__(self, num_colors, num_pegs):


        self.colors = num_colors
        self.pegs = num_pegs
        self.possible_pegs = self.possible_peg_responses()
        self.remaining = self.codes_list()

    def possible_peg_responses(self):

        responses = []
        for i in range(self.pegs + 1):
            for j in range(i + 1):
                responses.append((j, i - j))
        
            
        return responses
    
    def codes(self):

        return itertools.product(range(1, self.colors + 1), repeat=self.pegs)


    def codes_list(self): # return a LIST of codes

        return list(self.codes())

    def check_whites(self, previous_guess, new_guess, num_whites, num_blacks):

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

        
    def check_blacks(self, previous_guess, new_guess, num_blacks):

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

    def best_guess(self): # "max" function
        if len(self.remaining) == 0:
            return 'Something has gone wrong. \nYou might have an inconsistency in your answers. Type exit to exit.'

        if len(self.remaining) == 1:
            return self.remaining[0]
        most_removed = 0
        best = None
        for guess in self.codes():
            num_eliminated = self.least_elim(guess)
            if num_eliminated >= most_removed:
                most_removed = num_eliminated
                best = guess

        return best

    def best_guess_from_remaining(self): #less accurate, but faster
        
        if len(self.remaining) == 0:
            return 'Something has gone wrong. \nYou might have an inconsistency in your answers. Type exit to exit.'

        if len(self.remaining) == 1:
            return self.remaining[0]
        
        most_removed = 0
        best = None
        for guess in self.remaining:
            num_eliminated = self.least_elim(guess)
            if num_eliminated >= most_removed:
                most_removed = num_eliminated
                best = guess

        return best

    def random_guess(self):

        return self.remaining[random.randint(0, len(self.remaining) - 1)]
        

    def least_elim(self, guess): # "min" function
    
        least_removed = pow(self.colors, self.pegs)
        for response in self.possible_pegs:
            remove_count = self.count_not_matching(guess, response)
            if remove_count < least_removed:
                least_removed = remove_count
        
        return least_removed

    def count_not_matching(self, guess, response):

        whites, blacks = response
        remove_count = 0
        for combo in self.remaining:
            if not self.check_blacks(guess, combo, blacks) or not self.check_whites(guess, combo, whites, blacks):
                remove_count += 1

        return remove_count

    def eliminate(self, guess, response):

        whites, blacks = response
        new = list(self.remaining)
        for combo in self.remaining:
            if not self.check_blacks(guess, combo, blacks) or not self.check_whites(guess, combo, whites, blacks):

                new.remove(combo)
                
        self.remaining = new
                


# Opening guess 'book', provides optimal guesses.
# Useful for codes with large searchspaces
# Significant increase where (pow(num_pegs, num_colors)) > 200
def first_guess(num_colors, num_pegs):

    if num_pegs == 2:
        if num_colors <= 3:
            return (1, 1)
        else:
            return (1, 2)
    if num_pegs == 3:
        if num_colors == 2:
            return (1, 1, 1)
        elif num_colors == 3:
            return (1, 1, 2)
        else:
            return (1, 2, 3)
    if num_pegs == 4:
        if num_colors <= 3:
            return (1, 1, 1, 2)
        elif num_colors == 4:
            return (1, 1, 2, 3)
        else:
            return (1, 1, 2, 2)
    




