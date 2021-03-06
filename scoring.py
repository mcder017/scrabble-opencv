
class Blank:
    def __init__(self, l):
        #The letter that this blank has been assigned
        self.letter = l
    def __str__(self):
        return str(self.letter)


letter_points = {'a': 1,
                 'b': 3,
                 'c': 3,
                 'd': 2,
                 'e': 1,
                 'f': 4,
                 'g': 2,
                 'h': 4,
                 'i': 1,
                 'j': 8,
                 'k': 5,
                 'l': 1,
                 'm': 3,
                 'n': 1,
                 'o': 1,
                 'p': 3,
                 'q': 10,
                 'r': 1,
                 's': 1,
                 't': 1,
                 'u': 1,
                 'v': 4,
                 'w': 4,
                 'x': 8,
                 'y': 4,
                 'z': 10}

def get_letter_points(c):
    if isinstance(c, Blank):
        return 0 #Blanks are 0 points
    if c not in letter_points:
        raise ValueError
    return letter_points[c]


letter_mult= [[1,1,1,2,1,1,1,1,1,1,1,2,1,1,1],
              [1,1,1,1,1,3,1,1,1,3,1,1,1,1,1],
              [1,1,1,1,1,1,2,1,2,1,1,1,1,1,1],
              [2,1,1,1,1,1,1,2,1,1,1,1,1,1,2],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,3,1,1,1,3,1,1,1,3,1,1,1,3,1],
              [1,1,2,1,1,1,2,1,2,1,1,1,2,1,1],
              [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1],
              [1,1,2,1,1,1,2,1,2,1,1,1,2,1,1],
              [1,3,1,1,1,3,1,1,1,3,1,1,1,3,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [2,1,1,1,1,1,1,2,1,1,1,1,1,1,2],
              [1,1,1,1,1,1,2,1,2,1,1,1,1,1,1],
              [1,1,1,1,1,3,1,1,1,3,1,1,1,1,1],
              [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1]]

def get_letter_mult(x,y):
    return letter_mult[y][x]


word_mult =  [[3,1,1,1,1,1,1,3,1,1,1,1,1,1,3],
              [1,2,1,1,1,1,1,1,1,1,1,1,1,2,1],
              [1,1,2,1,1,1,1,1,1,1,1,1,2,1,1],
              [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1],
              [1,1,1,1,2,1,1,1,1,1,2,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [3,1,1,1,1,1,1,2,1,1,1,1,1,1,3],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,2,1,1,1,1,1,2,1,1,1,1],
              [1,1,1,2,1,1,1,1,1,1,1,2,1,1,1],
              [1,1,2,1,1,1,1,1,1,1,1,1,2,1,1],
              [1,2,1,1,1,1,1,1,1,1,1,1,1,2,1],
              [3,1,1,1,1,1,1,3,1,1,1,1,1,1,3]]

def get_word_mult(x,y):
    return word_mult[y][x]



