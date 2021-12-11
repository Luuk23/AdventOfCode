import numpy as np

with open("inputd11.txt") as file:
    m = np.genfromtxt(file, delimiter=1)

m = np.pad(m, pad_width=1, mode='constant', constant_values=-float("inf"))


def flash(m, coords, has_flashed):
    x, y = coords
    m[(x - 1):(x + 2), (y - 1):(y + 2)] += 1
    m[x][y] -= 1
    has_flashed[x][y] = True


has_flashed = np.zeros((len(m), len(m[0])), dtype=bool)
flashes = 0
step = 0
while True:
    step += 1
    m += 1
    has_flashed = np.zeros((len(m), len(m[0])), dtype=bool)
    while True:
        flash_points = np.transpose(np.where(m > 9))
        if flash_points.size == 0:
            break
        else:
            checker = 0
            for x, y in flash_points:
                if not has_flashed[x][y]:
                    flash(m, (x, y), has_flashed)
                    flashes += 1
                else:
                    checker += 1
            if checker == len(flash_points):
                break
    if np.all(has_flashed[1:-1, 1:-1]):
        break
    m[np.where(has_flashed)] = 0

print(flashes)
print(step)
