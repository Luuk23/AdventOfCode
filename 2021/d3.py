# import numpy as np
#
# with open("input3.txt") as file:
#
#     zeros1 = []
#     ones1 = []
#     zeros2 = []
#     ones2 = []
#     zeros3 = []
#     ones3 = []
#     zeros4 = []
#     ones4 = []
#     zeros5 = []
#     ones5 = []
#
#     # zeros = np.zeros(12)
#     # ones = np.zeros(12)
#
#     for i in range(12):
#
#         zeros = 0
#         ones = 0
#
#         for line in file:
#             line = line[:12]
#             print(line)
#
#             if int(line[i]) == 0:
#                 zeros += 1
#             elif int(line[i]) == 1:
#                 ones += 1
#             else:
#                 print('error')
#
#             if zeros > ones:
#
#
#
#
#
#
#
#
#
#         for i in range(len(line)):


with open("input3.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]



def find_number(file, index, starter):

    zeros = 0
    ones = 0
    current_winner = ""
    print(index)
    print(file)

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
        else:
            print('error 2')
    elif len(file) == 1:
        return file
    elif len(file) == 0:
        return 'error 0'

    for line in new_file:
        line = line[:12]

        if int(line[index]) == 0:
            zeros += 1
        elif int(line[index]) == 1:
            ones += 1
        else:
            print('error')

    print(zeros)
    print(ones)
    if zeros <= ones:
        return find_number(new_file, index+1, 0)
    else:
        return find_number(new_file, index+1, 1)



print(find_number(lines, 0, 0))
