import numpy as np

with open("inputd9.txt") as file:
    numbers = [n for n in file.read().splitlines()]

# Build border
size = len(numbers) + 2
numbers_bounded = np.zeros((size, size))
for ii in range(size):
    for jj in range(size):
        if ii == 0 or ii == size - 1 or jj == 0 or jj == size - 1:
            numbers_bounded[ii][jj] = 9
        else:
            numbers_bounded[ii][jj] = int(numbers[ii - 1][jj - 1])

# Find low points
sum_ = 0
low_points = []
for ii in range(1, size - 1):
    for jj in range(1, size - 1):
        if numbers_bounded[ii][jj] < numbers_bounded[ii - 1][jj] and numbers_bounded[ii][jj] < numbers_bounded[ii + 1][
            jj] and numbers_bounded[ii][jj] < numbers_bounded[ii][jj - 1] and numbers_bounded[ii][jj] < \
                numbers_bounded[ii][jj + 1]:
            sum_ += numbers_bounded[ii][jj] + 1
            low_points.append((ii, jj))

print(sum_)
print(low_points)


# Check if bigger number surrounding
def check_bigger(coords, matrix, dir, been_flag):
    ii, jj = coords

    if dir == 'up' and not been_flag[ii - 1][jj]:
        return matrix[ii][jj] < matrix[ii - 1][jj] != 9
    elif dir == 'down' and not been_flag[ii + 1][jj]:
        return matrix[ii][jj] < matrix[ii + 1][jj] != 9
    elif dir == 'left' and not been_flag[ii][jj - 1]:
        return matrix[ii][jj] < matrix[ii][jj - 1] != 9
    elif dir == 'right' and not been_flag[ii][jj + 1]:
        return matrix[ii][jj] < matrix[ii][jj + 1] != 9

    return False


# Recursively seek for all connecting bigger numbers
def get_basin_size(coords, matrix):
    global count
    count += 1
    ii, jj = coords
    been_flag[ii][jj] = True

    if check_bigger(coords, matrix, 'up', been_flag):
        get_basin_size((ii - 1, jj), matrix)
    if check_bigger(coords, matrix, 'right', been_flag):
        get_basin_size((ii, jj + 1), matrix)
    if check_bigger(coords, matrix, 'down', been_flag):
        get_basin_size((ii + 1, jj), matrix)
    if check_bigger(coords, matrix, 'left', been_flag):
        get_basin_size((ii, jj - 1), matrix)

    return count


basins = []
been_flag = np.zeros((size, size), dtype=bool)
for ii, jj in low_points:
    been_flag[ii][jj] = True
    count = 0
    basins.append(get_basin_size((ii, jj), numbers_bounded))

print(np.prod(sorted(basins)[-3:]))
