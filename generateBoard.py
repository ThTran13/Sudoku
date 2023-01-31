# Code to generate initial board for Sudoku
# All sudoku (normal) games start with 17 clues for unique solution

import numpy as np
import random as rand

class generateBoard:
    rows = 9
    cols = 9
    num_clues = 17

    def __init__(self):
        # a list of every coordinate on the board in tuple format
        self.all_coords = [(i, j) for i in range(generateBoard.rows)
                        for j in range(generateBoard.cols)]
        # generates board filled with zeros to start
        self.board = np.zeros((generateBoard.rows, generateBoard.cols))
        # initializes the clue tuples used in code
        self.clue_locs = []
        
    def clue_locations(self):  # will get 17 random locations for Board in tuples
        while len(set(self.clue_locs)) != generateBoard.num_clues:
            if self.all_coords[rand.randint(0, 80)] not in self.clue_locs:
                self.clue_locs.append(self.all_coords[rand.randint(0, 80)])
            else:
                pass
        # makes tuples of clue locations a list so that the elements can be indexed
        self.clue_locs = list(set(self.clue_locs))
        return self.clue_locs

    def displayBoard(self):
        # displays the board by placing the clues where the clue locations are
        # will make sure the clue placement and number is not invalid to the rules
        # of sudoku (each row and each column can only have 1 number 1-9)
        for location in self.clue_locations():
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            x = rand.randint(1, 9)
            while self.board[location[0]][location[1]] == 0:
                if x not in self.board[location[0], :] and x not in self.board[:, location[1]]:
                    self.board[location[0]][location[1]] = x
                else:
                    if x in nums:
                        nums.remove(x)
                        x = rand.choice(nums)
        return np.array(self.board).astype(int)

    def ClueChecker(self):
        # double checks that the number of clues on the generated board is 17
        counter = 0
        for i in range(generateBoard.rows):
            for j in range(generateBoard.cols):
                if self.displayBoard()[i][j] != 0:
                    counter += 1
        return counter

    def __str__(self):
        return f'Locations of Clues:\n{self.clue_locations()}'

board = generateBoard()
print(board.displayBoard())
