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
        print("Checking location ", city, ", Value = ", self.data[city])


board = Board(10,2)

print(board.size)