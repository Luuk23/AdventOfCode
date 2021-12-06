import numpy as np

with open("inputd5.txt") as file:

    coords = [n for n in file.read().splitlines()]
    print(coords)

field = np.zeros((1000, 1000))

for coor in coords:

    (first, second) = tuple(coor.split(" -> "))

    x1, y1 = [int(n) for n in first.split(",")]
    x2, y2 = [int(n) for n in second.split(",")]


    if x1 == x2:
        if y2 < y1:
            for i in range(y2, y1+1):
                field[x1][i] += 1
        elif y1 < y2:
            for i in range(y1, y2+1):
                field[x1][i] += 1
    elif y1 == y2:
        if x2 < x1:
            for i in range(x2, x1+1):
                field[i][y1] += 1
        elif x1 < x2:
            for i in range(x1, x2+1):
                field[i][y1] += 1
    else:
        # print(x1)
        # print(y1)
        # print(x2)
        # print(y2)
        if x1 < x2 and y1 < y2:
            while x1 <= x2:
                field[x1][y1] += 1
                #print((x1, y1))
                x1 += 1
                y1 += 1
        elif x1 < x2 and y1 > y2:
            while x1 <= x2:
                field[x1][y1] += 1
                #print((x1, y1))
                x1 += 1
                y1 -= 1
        elif x1 > x2 and y1 < y2:
            while x1 >= x2:
                field[x1][y1] += 1
                #print((x1, y1))
                x1 -= 1
                y1 += 1
        elif x1 > x2 and y1 > y2:
            while x1 >= x2:
                field[x1][y1] += 1
                #print((x1, y1))
                x1 -= 1
                y1 -= 1


sum = 0
for row in field:
    for col in row:
        if col >= 2:
            sum += 1

print(sum)