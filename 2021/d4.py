import numpy as np

with open("inputd4.txt") as file:

    bingo_nums = [int(n) for n in file.readline().split(",")]
    print(bingo_nums)

    all_boards = [line for line in file.read().splitlines() if line]
    print(all_boards)

    boards = []
    temp_board = []
    for row in range(len(all_boards)):

        if row % 5 == 0:
            temp_board = []

        temp_board.append([int(n) for n in all_boards[row].split()])

        if row % 5 == 4:
            boards.append(temp_board)


    print(boards)


    def check_board(lijst, nums):
        sum = 0
        checker = np.zeros((5, 5))
        for row in range(len(lijst)):
            for col in range(len(lijst[row])):
                if lijst[row][col] not in nums:
                    sum += lijst[row][col]
                else:
                    checker[row][col] = 1

        winner = 5

        if winner in checker.sum(axis=0) or winner in checker.sum(axis=1):
            return nums[-1] * sum
        else:
            return -1


    nums = []
    for n in bingo_nums:
        nums.append(n)

        boards_copy = boards.copy()
        for board in boards:
            result = check_board(board, nums)
            if result != -1:
                print(result)
                boards_copy.remove(board)

        boards = boards_copy
