from random import random
from numpy import array
from time import time

from Puzzle import Puzzle
import heapq

puzzle = array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [16, 10, 11, 12],
    [9, 13, 14, 15]
])

current = Puzzle(puzzle)
q = []
n = 0

t1 = time()
while not current.solved() and current.reachable():
    current.filterMove()
    for move in current.availableMove:
        child, direction = current.generate(move)
        prevPath = current.path
        child = Puzzle(child)
        child.getCost()
        child.prevMove = direction
        child.path = prevPath + [direction]
        heapq.heappush(q, (child.cost, random(), child))
        n += 1
    if len(q) > 0:
        current = heapq.heappop(q)[2]
    else:
        break
t2 = time()

if current.solved():
    print("Solusi:")
    current.showPuzzle()
    print("Jalur:")
    solvedPuzzle = Puzzle(puzzle)
    for move in current.path:
        print(">>> ", move.value)
        child, _ = solvedPuzzle.generate(move)
        child = Puzzle(child)
        child.showPuzzle()
        solvedPuzzle = child
    print("Jumlah simpul dibangkitkan: ", n)
else:
    print("Tidak dapat menemukan solusi")
print(f"Durasi: {round(t2 - t1, 6)} s")