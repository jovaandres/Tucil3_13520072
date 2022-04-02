from Solver import Solver


print("15-Puzzle Solver\n")
solver = Solver()
print("Select options: \n1. Read puzzle from file \n2. Generate puzzle")
option = int(input(">> "))
if option == 1:
    solver.readPuzzleFromFile()
elif option == 2:
    solver.generatePuzzle()
solver.solve()
solver.result()
