import random
import sys
import numpy as np

# Today we are going to make an interactive game in Python.
# This is going to be a game of noughts and crosses!

#  Initialise grid and collection of X's or O's needed to win a game.
grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
print(np.asarray(grid))  # To make the output represent a grid instead of a list of lists.
row_os = ["O", "O", "O"]
row_xs = ["X", "X", "X"]
coords_picked = []

# Create a loop to find all co-ordinates in our grid
all_coords = []
for x in range(3):
    for y in range(3):
        all_coords.append((x, y))

turn = 0
remaining_coords = []

while turn < 10:
    # Find status of each column
    column_1 = [row[0] for row in grid]
    column_2 = [row[1] for row in grid]
    column_3 = [row[2] for row in grid]

    # Find status of 2 diagonals
    main_diag = [row[i] for i, row in enumerate(grid)]
    counter_diag = [row[-i - 1] for i, row in enumerate(grid)]

    # Winning conditions for each player
    if (grid[0] == row_os or grid[1] == row_os or grid[2] == row_os) or (
            column_1 == row_os or column_2 == row_os or column_3 == row_os) or (main_diag == row_os) or (
            counter_diag == row_os):
        print("The computer has won!")
        sys.exit()
    elif (grid[0] == row_xs or grid[1] == row_xs or grid[2] == row_xs) or (
            column_1 == row_xs or column_2 == row_xs or column_3 == row_xs) or (main_diag == row_xs) or (
            counter_diag == row_xs):
        print("Well done, you have won!")
        sys.exit()
    else:
        # If nobody has won yet, take another turn
        if turn % 2 == 0:
            x_coord = input()
            y_coord = input()
            coords_picked.append((int(x_coord), int(y_coord)))
            grid[int(x_coord)][int(y_coord)] = "X"
            print(np.asarray(grid))
            turn += 1
        else:
            # Computer randomly picks a co-ordinate in the grid that has not been picked yet
            remaining_coords = list(set(all_coords) - set(coords_picked))
            comp_coords = random.choice(remaining_coords)
            grid[comp_coords[0]][comp_coords[1]] = "O"
            coords_picked.append((comp_coords[0], comp_coords[1]))
            print(comp_coords)
            print(np.asarray(grid))
            turn += 1

print("A draw?! We must play again!")
