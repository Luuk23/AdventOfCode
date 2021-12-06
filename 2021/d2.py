with open("inputd2.txt") as file:
    horizontal = 0
    vertical = 0
    aim = 0
    for line in file:
        value = int(line[-2])
        instruction = line[:-2]
        print(instruction)

        if instruction == 'forward ':
            vertical += aim * value
            horizontal += value
        elif instruction == 'down ':
            # vertical += value
            aim += value
        elif instruction == 'up ':
            # vertical -= value
            aim -= value
        else:
            print("error")
            break

print(horizontal * vertical)