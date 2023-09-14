# The following code define a function that creates a grid, taking in a '#', and '-' grid as an input where:

# '#' = mine (dangerous cell)

# '-' = safe cell

# The program outputs a grid where each dash is replaced by a digit, indicating the numebr of 'mines' immediately adjacent to the to the spot. (Horizontally or vertically, and diagonally)

# Example of an input:

# [ ["-", "-", "-", "#"],
#   ["-", "-", "#", "-"],
#   ["#", "#", "-", "#"],
#   ["-", "-", "-", "#"],
#   ["#", "-", "#", "-"],
#   ["#", "-", "#", "#"] ]

# Example of the expected output:

# [ ["0", "1", "2", "#"],
#   ["2", "3", "#", "3"],
#   ["#", "#", "4", "#"],
#   ["2", "1", "4", "#"],
#   ["#", "3", "#", "4"],
#   ["#", "3", "#", "#"] ]


def generate_minesweeper_board(grid):
    rows = len(grid)
    cols = len(grid[0])
    output = [["0" for _ in range(cols)] for _ in range(rows)]

    for row, row_values in enumerate(grid):
        for col, cell in enumerate(row_values):
            if cell == "#":
                output[row][col] = "#"

    for row, row_values in enumerate(grid):
        for col, cell in enumerate(row_values):
            if cell == "#":
                continue

            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    new_row, new_col = row + dx, col + dy

                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if grid[new_row][new_col] == "#":
                            count += 1

            output[row][col] = str(count)

    return output


# Adjust this input grid accordingly, to test.
input_grid = [
    ["#", "-", "-", "-"],
    ["-", "-", "#", "-"],
    ["#", "#", "-", "-"],
    ["-", "-", "-", "-"],
    ["#", "-", "-", "-"],
    ["#", "-", "-", "-"],
]

output_grid = generate_minesweeper_board(input_grid)
for row in output_grid:
    print(row)
