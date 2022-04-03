import heapq
from random import random, shuffle
from time import time
from numpy import array

from Puzzle import Puzzle


class Solver:
    def __init__(self) -> None:
        self.origin = None
        self.current = None
        self.path = []
        self.solved = False
        self.raisedBranch = 0
        self.timeElapsed = 0
        self.queue = []

    def solveable(self, puzzle):
        puzzle = array(puzzle).reshape(4, 4)
        puzzle = Puzzle(puzzle)
        return puzzle.reachable()

    def readPuzzleFromFile(self):
        puzzle = []
        filename = input("Input filename: ")
        file = open(r"../test/" + filename, "r")
        for line in file.readlines():
            row = line.removesuffix('\n').split(' ')
            puzzle.append(row)
        puzzle = array(puzzle).astype(int)
        self.origin = puzzle

    def generatePuzzle(self, solveable=None):
        puzzle = [i+1 for i in range(16)]
        shuffle(puzzle)
        if solveable == True:
            while not self.solveable(puzzle):
                shuffle(puzzle)
        self.origin = array(puzzle).reshape(4, 4)

    def preSolvedOutput(self, current):
        totalKurangI = 0
        print("Puzzle input:")
        current.showPuzzle()
        for i in range(1, 17):
            kurangI = current.kurang(i)
            print(f"Kurang {i} = {kurangI}")
            totalKurangI += kurangI
        print(
            f"Total kurang I + X = {totalKurangI + sum(current.posisi(16)) % 2}")
        print("Calculating...\n")

    def solve(self):
        current = Puzzle(self.origin)
        self.preSolvedOutput(current)
        if not current.reachable():
            return
        t1 = time()
        while not current.solved():
            current.filterMove()
            for move in current.availableMove:
                child, direction = current.generate(move)
                prevPath = current.path
                child = Puzzle(child)
                child.getCost()
                child.prevMove = direction
                child.path = prevPath + [direction]
                heapq.heappush(self.queue, (child.cost, random(), child))
                self.raisedBranch += 1
            if len(self.queue) > 0:
                current = heapq.heappop(self.queue)[2]
            else:
                break
        t2 = time()
        self.timeElapsed = t2 - t1
        self.solved = current.solved()
        self.path = current.path

    def result(self):
        if self.solved:
            langkah = 0
            solvedPuzzle = Puzzle(self.origin)
            print("Path:")
            [print(i.value, end=' ') for i in self.path]
            print("\n")
            for move in self.path:
                print(f"Step-{langkah}")
                print(">> ", move.value)
                child, _ = solvedPuzzle.generate(move)
                child = Puzzle(child)
                child.showPuzzle()
                solvedPuzzle = child
                langkah += 1
            print("Total raised nodes: ", self.raisedBranch)
        else:
            print("Can't find a solution")
        print(f"Time elapsed: {round(self.timeElapsed, 6)} s")
        print("THANK YOU!!!")
