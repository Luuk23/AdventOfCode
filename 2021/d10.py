import numpy as np

with open("inputd10.txt") as file:
    lines = [n for n in file.read().splitlines()]

char_mapping = {'(': ')', '<': '>', '[': ']', '{': '}'}
score_mapping = {')': 3, ']': 57, '}': 1197, '>': 25137}
complete_score_mapping = {')': 1, ']': 2, '}': 3, '>': 4}

score = 0
complete_scores = []
for line in lines:
    openers = ""
    corrupt_flag = False
    for el in line:
        if el in ['(', '{', '[', '<']:
            openers += el
        elif el in [')', '}', ']', '>'] and el == char_mapping[openers[-1]]:
            openers = openers[:-1]
        else:
            score += score_mapping[el]
            corrupt_flag = True
            break

    if not corrupt_flag:
        completing_score = 0
        for el in reversed(openers):
            completing_score *= 5
            completing_score += complete_score_mapping[char_mapping[el]]
        complete_scores.append(completing_score)

print(score)
print(np.median(complete_scores))
