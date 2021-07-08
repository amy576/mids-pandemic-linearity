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
        print("New board: ", self.data)

        print(caseload)
        return caseload



board = Board(10,2)

board.move(0)

board.move(1)

board.move(2)