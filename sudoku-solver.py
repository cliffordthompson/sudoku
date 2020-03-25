# ***************************************************************************
# Copyright (c) 2020 Clifford Thompson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ***************************************************************************

import numpy as np

# ***************************************************************************
# Description:
#   Some example puzzles. 0 represents an unsolved location.
# ***************************************************************************
#
puzzles = [\
    [[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,7,9]],
\
    [[0,0,0,0,0,5,0,3,0],
     [0,0,0,2,4,0,0,0,9],
     [0,9,0,6,3,0,2,0,0],
     [9,2,0,1,5,0,0,8,6],
     [0,0,1,7,6,2,3,0,0],
     [6,4,0,0,8,9,0,5,2],
     [0,0,5,0,9,1,0,4,0],
     [1,0,0,0,2,6,0,0,0],
     [0,8,0,5,0,0,0,0,0]],
\
     [[5,3,0,0,7,0,0,0,0],
     [6,0,0,1,9,5,0,0,0],
     [0,9,8,0,0,0,0,6,0],
     [8,0,0,0,6,0,0,0,3],
     [4,0,0,8,0,3,0,0,1],
     [7,0,0,0,2,0,0,0,6],
     [0,6,0,0,0,0,2,8,0],
     [0,0,0,4,1,9,0,0,5],
     [0,0,0,0,8,0,0,9,7]]]


# ***************************************************************************
# Description:
#   This function determines if a number is possible for particular
#   puzzle row.
#
# Inputs:
#   puzzle [9x9 in array] The puzzle to check against
#   row    [int] The integer row in the puzzle to check
#   number [int] The number to check the possibility for
# Outputs:
#   None
# Returns:
#   True if the number is possible for a row, False otherwise.
# ***************************************************************************
#
def possibleForRow(puzzle,row,number) :
    for column in range(0,9) :
        if puzzle[row][column] == number :
            return False
    return True

# ***************************************************************************
# Description:
#   This function determines if a number is possible for particular
#   puzzle column.
#
# Inputs:
#   puzzle [9x9 in array] The puzzle to check against
#   column [int] The integer column in the puzzle to check
#   number [int] The number to check the possibility for
# Outputs:
#   None
# Returns:
#   True if the number is possible for a column, False otherwise.
# ***************************************************************************
#
def possibleForColumn(puzzle,column,number) :
    for row in range(0,9) :
        if puzzle[row][column] == number :
            return False
    return True

# ***************************************************************************
# Description:
#   This function determines if a number is possible for particular
#   puzzle square, give a row/column location.
#
# Inputs:
#   puzzle [9x9 in array] The puzzle to check against
#   row    [int] The integer row within a square to check
#   column [int] The integer column in the square to check
#   number [int] The number to check the possibility for
# Outputs:
#   None
# Returns:
#   True if the number is possible for a square, False otherwise.
# ***************************************************************************
#
def possibleForSquare(puzzle,row,column,number) :
    firstSquareRow    = (row//3)*3
    firstSquareColumn = (column//3)*3

    for squareRow in range(0,3) :
        for squareColumn in range(0,3) :
            if puzzle[firstSquareRow + squareRow][firstSquareColumn + squareColumn] == number :
                return False
    return True

# ***************************************************************************
# Description:
#   This function determines if a number is possible for a particular
#   location in a puzzle
# Inputs:
#   puzzle [9x9 array] The puzzle to check against
#   row    [int] The integer row of the location to check
#   column [int] The integer column of the location to check
#   number [int] The number to check the possiblity for
# Outputs:
#   None
# Returns:
#   True if the number is possible for the location, False otherwise
# ***************************************************************************
#
def possible(puzzle,row,column,number) :
    return \
        possibleForRow(puzzle,row,number) and \
        possibleForColumn(puzzle,column,number) and \
        possibleForSquare(puzzle,row,column,number)

# ***************************************************************************
# Description:
#   This function attempts to solve a given Sudoku puzzle by brute force in
#   a recursive manner. If the function cannot solve the puzzle from a given
#   position, it will return the puzzle to it's original state.
# Inputs:
#   puzzle [9x9 array] The puzzle to solve
# Outputs:
#   puzzle [9x9 array] The updated solved puzzle
# Returns:
#   None
# ***************************************************************************
#
def bruteForceSolver(puzzle) :
    for row in range(9) :
        for column in range(9) :
            if puzzle[row][column] == 0 :
                for number in range(1,10) :
                    if possible(puzzle,row,column,number) :
                        puzzle[row][column] = number
                        if bruteForceSolver(puzzle) :
                            return True
                        puzzle[row][column] = 0
                return False
    return True

# ***************************************************************************
# Some sample tests. In the future, the puzzle will be passed as a command line
# parameter
# ***************************************************************************
#
def main() :
    for index, puzzle in enumerate(puzzles) :
        print('\n=========== Puzzle {} Solution ===========\n'.format(index))
        if bruteForceSolver(puzzle):
            print(np.matrix(puzzle))
        else :
            print('No solution!\n')

if __name__== "__main__": main()
