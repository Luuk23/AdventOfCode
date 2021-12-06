with open("inputd1.txt") as file:
    start = int(file.readline())
    count = 0
    for line in file:
        if int(line) > start:
            count += 1

        start = int(line)

print(count)

with open("inputd1.txt") as file:

    f = int(file.readline())
    s = int(file.readline())
    t = int(file.readline())
    total = f + s + t

    count = 0
    for line in file:

        if int(line) + s + t > total:
            count += 1

        f = s
        s = t
        t = int(line)
        total = f+s+t

print(count)