# Solving 15-Puzzle Problems with the Branch and Bound Algorithm

## Table of Contents
- [General Info](#general-information)
- [Screenshots](#screenshots)
- [Installation](#installation)

## General Information
This is a program to get the solution of 15-puzzle using branch and bound algorithm. 
The program can accept puzzles from text files and also provides a function to generate random puzzles. As a note, the empty tiles in the puzzle are marked with the number 16. Sample text files can be seen in the test folder.
The initial puzzle will be initiated as the initial node, then the program will determine the possible direction of motion of the empty tile based on the position and direction of movement of the previous node. For each direction, the program will generate a new node as long as it has not found a solution. Each node will be put into a priority queue based on its cost.

## Screenshots


## Installation
#### Before you start <br><br>
Before getting started, you should have the following installed and running:

- [X] Python 3.10.0 (https://www.python.org/)
- [X] NumPy (https://numpy.org/)
#### Template and Dependencies

* Clone this repository:

  ```
  $ git clone https://github.com/jovaandres/15Puzzle.git
  ```

* Install dependencies <br>
Installation can be done via the package installer for python ([pip](https://pypi.org/project/pip/))

* Run the program

```
In the src folder
$ py main.py
```

```
DONE!
```

### Author
Jova Andres Riski Sirait (13520072)
