class BoardSolver:
    
    def __init__(self, board):
        self.board = board

    def empty_location(self):
        #combs through rows
        for i in range(len(self.board)):
        #combs through columns
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                #returns position of empty space
                    return (i, j)
        return 0

    #checks to see if inputted value in board works
    def is_valid(self, number, position):
        #check row
        for i in range(9):
            #checks to see if elements in row match inputted number or is number in the position we just inputted
            if self.board[[position][i] == number and position[1] != i]:
                return False

        #check column
        for i in range(9):
            #checks to see if elements in column match inputted number or is the position just inputted
            if self.board[[position][i] == number and position[1] != i]:
                return False

        #determine which box we are in
        box_x = position[1] // 3
        box_y = position[0] // 3

        #define bounds of the box based on position value
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                #check values within defined box for the number value
                if self.board[i][j] == number and (i, j) != position:
                    return False
        return True

    #main method
    def solve(self):
        find = BoardSolver.empty_location()
        #first check if board is filled
        if find != True:
            return True
        else:
            row, col = find
            #checks board
            for i in range(1, 10):
                if BoardSolver.is_valid(i, (row, col)):
                    self.board[row][col] = i
                    if BoardSolver.solve():
                        return True
                    self.board[row][col] = 0
