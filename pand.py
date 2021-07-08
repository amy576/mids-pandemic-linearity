class Board:
    def __init__(self, n, epicenter):
        ## size is the number of cities
        self.size = n
        try:
            self.data = [0] * n
        except TypeError:
            print("the first arugment must be an integer")

        ## epicenter is where the pandemic starts, with caseload 1
        try:
            self.data[epicenter] = 1
        except TypeError:
            print("the second argument must be an integer")
        self.epicenter = epicenter
        print("Creating board: ", self.data)

    ## this inspects a city
    def move(self, city):
        ## return the caseload discovered
        caseload = self.data[city]
        print("Checking location {0}, Value = {1}".format(city, caseload))

        ## pandemic spreads
        epi = self.epicenter
        self.data[epi] += 1
        for i in range(1, self.data[epi]):
            if epi+i < len(self.data):
                self.data[epi+i] += 1
            if epi-i >= 0:
                self.data[epi-i] += 1
        # print("New board: ", self.data)

        return caseload


class Solver:
    def __init__(self, board):
        self.solve(board)

    def solve(self, board):
        if isinstance(board, Board) == False:
            print("first argument must be class type Board")
        else:
            n = board.size
            guesses = 0
            caseload = 0

            while caseload == 0:

                cities = []
                splits = 2 * (guesses + 1)
                for i in range(1, splits):
                    cities.append((int(n/splits))*i)

                for c in cities:
                    city = c
                    guesses += 1
                    caseload = board.move(city)

                    ## epicenter will always be equal to number of guesses if epicenter caseload starts at 1
                    if caseload == guesses:
                        print("Found it after {0} guesses: {1}".format(guesses,city))
                        return city

                    ## once a non-zero caseload is found, based on the number of guesses and the fact that the caseload
                    ## spreads from the epicenter at a rate of 1, we know how many spaces away from the non-zero caseload
                    ## the epicenter is
                    elif caseload > 0:
                        diff = guesses - caseload
                        guesses += 1

                        ## we need to check both "left" and "right" of this caseload though
                        check1 = board.move(city+diff)
                        if check1 == guesses:
                            print("Found it after {0} guesses: {1}".format(guesses,city+diff))
                            return city+diff
                        else:
                            print("Found it after {0} guesses: {1}".format(guesses,city-diff))
                            return city-diff

                
# board = Board(10,2)
# board = Board(10,3)
# board = Board(1000,666)
# board = Board(5000,4997)
# board = Board(5000,4)

# solver = Solver(board)

# board.move(0)

# board.move(1)

# board.move(2)