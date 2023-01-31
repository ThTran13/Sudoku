from tkinter import *
from solverSu import solver
from generate_sudoku import generate
import numpy as np
from generateBoard import generateBoard
# from boardSolver import boardSolver


class sudoku_gui():
    def __init__(self):
        self.board_solution = []    #array to store the board solution
        self.board_ques = []    #array to store the unsolved board
        self.cells = {} #a set that put inside a grid to accept number

    #create a 3x3 grid in a 9x9 sudoku
    def draw3x3Grid(self, row, column, bgcolor):
        for i in range(3):
            for j in range(3):
                #allow user to enter digit with validate key using ValidateNumber method
                e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
                #create a grid for each number in a 3x3 grid
                #ipady, ipadx is the width and length of the grid
                #pady padx is the space between the grid
                e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=12, ipadx = 11)
                self.cells[(row + i + 1, column + j + 1)] = e

    #using the 3x3 grid to create a 9x9 grid by using 2 loops
    def draw9x9Grid(self):
        color = "#eaf5ff"
        for rowNo in range(1, 10, 3):
            for colNo in range(0, 9, 3):
                sudoku_gui.draw3x3Grid(self, rowNo, colNo, color)
                if color == "#eaf5ff":
                    color = "#d0d1ff"
                else:
                    color = "#eaf5ff"

    #clear value by creating a loop that goes through all the grid and delete the number in it
    def clearValues(self):
        errLabel.configure(text="")
        solvedLabel.configure(text="")
        for row in range(2, 11):
            for col in range(1, 10):
                cell = self.cells[(row, col)]
                cell.delete(0, "end")

    #a method to check the values
    def check_values(self):
        errLabel.configure(text="")
        solvedLabel.configure(text="")
        board = []
        #assigning sol_grid to the array that store the board solution so that the original array will be modified
        sol_grid = self.board_solution
        print(sol_grid)
        
        for row in range(2, 11):
            rows = []
            for col in range(1, 10):
                num = sol_grid[row - 2][col - 1]
                val = (self.cells[(row, col)]).get()
                if val == '':
                    rows.append(0)
                    num_row = row - 1#the value of row
                    num_col = col #the value of col
                    errLabel.configure(text="wrong input at row " + str(num_row) + " and column " + str(num_col))
                    break
                if val != num:
                    rows.append(int(val))
                    num_row = row - 2 #the value of row
                    num_col = col - 1 #the value of col
                    errLabel.configure(text="wrong input at row " + str(num_row) + " and column " + str(num_col))
                    break
                else:
                    rows.append(int(val))
            board.append(rows)
            print(board)
        check = np.array_equal(np.array(sol_grid), np.array(board))
        print(check)
        print(board)
        if check is True:
            solvedLabel.configure(text="Board is Solve")
        else:
            solvedLabel.configure(text="Board not Solve")

    def get_newBoard(self):
        errLabel.configure(text="")
        solvedLabel.configure(text="")
        for row in range(2, 11):
            for col in range(1, 10):
                cell = self.cells[(row, col)]
                cell.delete(0, "end")

        self.board_ques = []
        self.board_solution = []
        grid = generate().generate_board()
        for row in range(2, 11):
            rows = []
            for col in range(1, 10):
                if grid[row - 2][col - 1] != 0:
                    self.cells[(row, col)].insert(0, grid[row - 2][col - 1])
                    val = (self.cells[(row, col)]).get()
                    rows.append(int(val))
                else:
                    rows.append(0)
            self.board_ques.append(rows)
        self.board_solution = solver(self.board_ques).getSolution()
        print("solution: ", self.board_solution)
        solvedLabel.configure(text="New Board Update")


    # #method to get a random generated sudoku board
    # def get_newBoard(self):
    #     errLabel.configure(text="")
    #     solvedLabel.configure(text="")

    #     #clear all the values on the board
    #     for row in range(2, 11):
    #         for col in range(1, 10):
    #             cell = self.cells[(row, col)]
    #             cell.delete(0, "end")

    #     #call the generator Board class
    #     grid = generateBoard().displayBoard()
    #     for row in range(2, 11):
    #         rows = []
    #         for col in range(1, 10):
    #             if grid[row - 2][col - 1] != 0:
    #                 self.cells[(row, col)].insert(0, grid[row - 2][col - 1])
    #                 val = (self.cells[(row, col)]).get()
    #                 rows.append(int(val))
    #             else:
    #                 rows.append(0)
    #         self.board_ques.append(rows) #append the values into board_ques array to store the unsolved sudokuboard
        
    #     #display the label
    #     solvedLabel.configure(text="New Board Update")

    #     self.board_solution = solver(self.board_ques).getSolution()
    #     #print("solution: ", self.board_solution)
        


    def solve_board(self):
        errLabel.configure(text="")
        solvedLabel.configure(text="")
        for row in range(2, 11):
            for col in range(1, 10):
                cell = self.cells[(row, col)]
                cell.delete(0, "end")

        board = self.board_solution
        if board is not False:
            for row in range(2, 11):
                for col in range(1, 10):
                    self.cells[(row, col)].delete(0, "end")  # delete existing value from the cells
                    self.cells[(row, col)].insert(0, board[row - 2][col - 1])  # inserting the solution at the index
            solvedLabel.configure(text="Sudoku Solved")
        else:
            errLabel.configure(text="No Solution for this sudoku!")


root = Tk()
root.geometry("522x580") #the size of the GUI
root.title("Sudoku Solver") #title of the GUI
label = Label(root, text="Play Sudoku").grid(row=0, column=1, columnspan=10) #create a label
errLabel = Label(root, text="", fg="red")  # create error label
errLabel.grid(row=15, column=1, columnspan=10, pady=5)  #assigning error label with size and position
solvedLabel = Label(root, text="", fg="green") #creating a solve label
solvedLabel.grid(row=16, column=1, columnspan=10, pady=5) #assigning solve label with size and position


s = sudoku_gui()

#a method that only allow user to enter a digit on each grid and it has to be less than 10
def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out


reg = root.register(ValidateNumber)
#create multiple buttons
# check user input solution
btn = Button(root, command=s.check_values, text="Check", width=10)
btn.grid(row=18, column=2, columnspan=3, pady=10)

# click to solve the original sudoku generated
btn = Button(root, command=s.solve_board, text="Solve", width=10)
btn.grid(row=19, column=2, columnspan=3, pady=5)

# click to get generate new board
btn = Button(root, command=s.get_newBoard, text="New Board", width=10)
btn.grid(row=18, column=6, columnspan=3, pady=10)

# click to clear values
btn = Button(root, command=s.clearValues, text="Clear", width=10)
btn.grid(row=19, column=6, columnspan=3, pady=5)

s.draw9x9Grid()
root.mainloop()