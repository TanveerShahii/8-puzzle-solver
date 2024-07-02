# 8-Puzzle Solver

This Python program implements the A* search algorithm to solve the 8-puzzle game, utilizing the Manhattan distance as a heuristic measure.

## Requirements

- Python 3.x installed on your system.

## Installation

No additional libraries are required to run this program, just a standard Python 3 installation.

## How to Run the Program

1. Ensure Python 3.x is installed on your computer.
2. Download the `8_puzzle_solver.py` file to a directory on your computer.
3. Open your command prompt (Windows) or terminal (macOS/Linux).
4. Navigate to the directory where you saved the file. For example:
   ```bash
   cd path/to/directory

You will be prompted to enter the start state and goal state of the puzzle. Each state must be entered row by row with numbers ranging from 0 (blank) to 8, separated by spaces. For example:
mathematica

Enter the start state (use 0 for blank):
Enter row 1 (three numbers separated by spaces): 1 2 3
Enter row 2 (three numbers separated by spaces): 4 5 6
Enter row 3 (three numbers separated by spaces): 0 7 8

Input Format
Input each row of the puzzle as three integers separated by spaces.
Each number should be unique and between 0 and 8, where 0 represents the blank space.

Output
The program will output the series of moves to solve the puzzle from the start state to the goal state, showing each state after the move. If the puzzle is unsolvable, the program will notify the user with "No solution found."

Example
Input:

Start State:

1 2 3
4 5 6
0 7 8

Goal State:
1 2 3
4 5 6
7 8 0
Output:

mathematica
Move Down:
1 2 3
4 5 6
7 0 8

Move Right:
1 2 3
4 5 6
7 8 0