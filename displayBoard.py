import numpy as np

class DisplayBoard:
    def __init__(self) -> None:
        pass
    
    def getEachLine(outerArr, innerArr, Matrix):  
        ele = Matrix[outerArr][innerArr].reshape(9,1)
        return ele

    def printBoard(Matrix):
        arr1 = []
        #creating a frame for the board
        for line in range(9):
            print("    ", end = "")
            for i in range(9):
                print("-------", end = " ")

            print("\n   |", end = "")
            for i in range(9):
                print("       |", end = "")
            print("\n", end = "")

            #inserting numbers in each box created 
            if line < 3:
              arr1 = DisplayBoard.getEachLine(0, line ,x)
              print("   |", end="")
              for num in range(9):
                    print(f'{arr1[num][0] : >4}', end = "   |")
            elif line < 6:
                arr1 = DisplayBoard.getEachLine(1, line%3 ,x)
                print("   |", end="")
                for num in range(9):
                    print(f'{arr1[num][0] : >4}', end = "   |")
            else:
                arr1 = DisplayBoard.getEachLine(2, line%3 ,x)
                print("   |", end="")
                for num in range(9):
                    print(f'{arr1[num][0] : >4}', end = "   |")
    

            print("\n   |", end = "")
            for i in range(9):
                print("       |", end = "")
            print("\n", end = "")
        print("    ", end = "")
        for i in range(9):
            print("-------", end = " ")

            


# test array
y = np.random.randint(1,10, size=81)
x = y.reshape((3,3,9))
print(x)

# t = x[0][0].reshape(9,1)
# print(t)
# t = x[0][1].reshape(9,1)
# print(t)
# t = x[0][2].reshape(9,1)
# print(t)

DisplayBoard.printBoard(x)