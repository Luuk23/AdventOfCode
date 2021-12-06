with open("input3.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


def find_number(file, index, starter):

    zeros = 0
    ones = 0

    new_file = file.copy()
    if index != 0:
        for line in file:
            if int(line[index-1]) != starter:
                new_file.remove(line)

    if len(file) == 2:
        if int(file[0][index-1]) == 1:
            return file[0]
        elif int(file[1][index-1]) == 1:
            return file[1]
    elif len(file) == 1:
        return file

    for line in new_file:
        line = line[:12]
        if int(line[index]) == 0:
            zeros += 1
        elif int(line[index]) == 1:
            ones += 1

    if zeros <= ones:
        return find_number(new_file, index+1, 0)
    else:
        return find_number(new_file, index+1, 1)


print(find_number(lines, 0, 0))
