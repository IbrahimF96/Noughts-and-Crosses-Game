import random
import sys

print("Welcome to Noughts and Crosses! Let's Play!")
SIDE_LENGTH = 3


def format_grid(grid):
    return "\n".join("  ".join(row) for row in grid)


grid = [["_"] * SIDE_LENGTH for _ in range(SIDE_LENGTH)]
row_os = ["O"] * SIDE_LENGTH
row_xs = ["X"] * SIDE_LENGTH
coords_picked = set()

print(format_grid(grid))  # To make the output represent a grid instead of a list of lists.

# Create a loop to find all co-ordinates in our grid
all_coords = set()
for x in range(SIDE_LENGTH):
    for y in range(SIDE_LENGTH):
        all_coords.add((x, y))

turn = 0
remaining_coords = set()

while turn < 10:
    # Find status of each column
    columns = [[row[i]
               for row in grid]
               for i in range(SIDE_LENGTH)]

    # Find status of 2 diagonals
    main_diag = [row[i] for i, row in enumerate(grid)]
    counter_diag = [row[-i - 1] for i, row in enumerate(grid)]

    # Winning conditions for each player
    if any((any(row == row_os for row in grid),
            any(col == row_os for col in columns),
            any(diag == row_os for diag in [main_diag, counter_diag]))):
        print("The computer has won!")
        sys.exit()
    elif any((any(row == row_xs for row in grid),
              any(col == row_xs for col in columns),
              any(diag == row_xs for diag in [main_diag, counter_diag]))):
        print("Well done, you have won!")
        sys.exit()
    else:
        # If nobody has won yet, take another turn
        if turn % 2 == 0:
            # Checking for invalid inputs
            while True:
                try:
                    x_coord = int(input("\nPlease enter your x coordinate: \n"))
                    y_coord = int(input("Please enter your y coordinate: \n"))
                    if (x_coord, y_coord) in coords_picked:
                        raise ValueError
                    grid[x_coord][y_coord] = "X"
                    break
                except (IndexError, ValueError):
                    print("Oops! That was not valid input, please input a number in the grid")

            coords_picked.add((x_coord, y_coord))
            print(format_grid(grid))
            turn += 1
        else:
            # Computer randomly picks a co-ordinate in the grid that has not been picked yet
            remaining_coords = all_coords - coords_picked
            comp_coords = random.choice(list(remaining_coords))
            grid[comp_coords[0]][comp_coords[1]] = "O"
            coords_picked.add((comp_coords[0], comp_coords[1]))
            print("\n")
            print(format_grid(grid))
            turn += 1

print("A draw?! We must play again!")
