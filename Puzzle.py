from numpy import array, array_equal, copy, where
from Direction import Direction


class Puzzle:
    def __init__(self, puzzleData) -> None:
        self.puzzle = puzzleData
        self.availableMove = []
        self.cost = 0
        self.path = []
        self.prevMove = None
        self.solution = array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ])

    def filterMove(self):
        blankPosition = where(self.puzzle == 16)
        blankPosition = (blankPosition[0][0], blankPosition[1][0])
        self.availableMove = [Direction.UP,
                              Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        if blankPosition[0] == 0:
            self.availableMove.remove(Direction.UP)
        if blankPosition[0] == 3:
            self.availableMove.remove(Direction.DOWN)
        if blankPosition[1] == 0:
            self.availableMove.remove(Direction.LEFT)
        if blankPosition[1] == 3:
            self.availableMove.remove(Direction.RIGHT)
        if self.prevMove != None and self.prevMove in self.availableMove:
            opposite = Direction.opposite(self.prevMove)
            self.availableMove.remove(opposite)
    
    def getCost(self):
        intersect = where((self.puzzle == self.solution), 0, 1)
        self.cost = intersect.sum()

    def posisi(self, i):
        x = where(self.puzzle == i)
        return x[0][0], x[1][0]

    def kurang(self, i):
        total = 0
        for j in range(4):
            for k in range(4):
                if self.puzzle[j][k] < i and self.posisi(self.puzzle[j][k]) > self.posisi(i):
                    total += 1
        return total

    def generate(self, direction):
        if direction == Direction.UP:
            return self.generateUp()
        elif direction == Direction.DOWN:
            return self.generateDown()
        elif direction == Direction.LEFT:
            return self.generateLeft()
        elif direction == Direction.RIGHT:
            return self.generateRight()

    def generateLeft(self):
        child = copy(self.puzzle)
        x, y = self.posisi(16)
        child[x][y], child[x][y - 1] = child[x][y - 1], child[x][y]
        return child, Direction.LEFT

    def generateRight(self):
        child = copy(self.puzzle)
        x, y = self.posisi(16)
        child[x][y], child[x][y + 1] = child[x][y + 1], child[x][y]
        return child, Direction.RIGHT

    def generateUp(self):
        child = copy(self.puzzle)
        x, y = self.posisi(16)
        child[x][y], child[x - 1][y] = child[x - 1][y], child[x][y]
        return child, Direction.UP

    def generateDown(self):
        child = copy(self.puzzle)
        x, y = self.posisi(16)
        child[x][y], child[x + 1][y] = child[x + 1][y], child[x][y]
        return child, Direction.DOWN

    def reachable(self):
        totalKurangI = sum([self.kurang(i) for i in range(1, 17)])
        a, b = self.posisi(16)
        X = (a + b) % 2
        return (totalKurangI + X) % 2 == 0

    def solved(self):
        return array_equal(self.puzzle, self.solution)

    def showPuzzle(self):
        newPuzzle = copy(self.puzzle)
        newPuzzle[newPuzzle == 16] = 0
        print(newPuzzle)
