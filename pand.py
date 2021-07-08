class Board:
    def __init__(self, n, epicenter):
        ## size is the number of cities
        self.size = n
        self.data = [0] * n

        ## epicenter is where the pandemic starts, with caseload 1
        self.data[epicenter] = 1
        self.epicenter = epicenter
        print("Creating board: ", self.data)



board = Board(10,2)

print(board.size)