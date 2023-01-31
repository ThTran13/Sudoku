from gui import sudoku_gui
from boardSolver import BoardSolver
from generateBoard import generateBoard
from displayBoard import DisplayBoard 
from tkinter import *


#testing array
# y = np.random.randint(1, 10, size=81)
# x = y.reshape((3, 3, 9))

board = generateBoard()
print(board.displayBoard())

solver = BoardSolver(board)
print(solver.solve())

DisplayBoard.printBoard(solver)
# DisplayGui.draw9x9Grid()
# DisplayGui.root.mainloop()

root = Tk()
root.geometry("522x550")  #the size of the GUI
root.title("Sudoku Solver")  #title of the GUI
label = Label(root, text="Play Sudoku").grid(row=0, column=1,
                                             columnspan=10)  #create a label
errLabel = Label(root, text="", fg="red")  # create error label
errLabel.grid(row=15, column=1, columnspan=10,
              pady=5)  #assigning error label with size and position
solvedLabel = Label(root, text="", fg="green")  #creating a solve label
solvedLabel.grid(row=15, column=1, columnspan=10,
                 pady=5)  #assigning solve label with size and position

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
