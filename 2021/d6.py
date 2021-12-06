import numpy as np

with open("inputd6.txt") as file:
    init_fish = np.array([int(n) for n in file.readline().split(",")])
    print(init_fish)

fish_count = np.zeros(9)
for fish in init_fish:
    fish_count[fish] += 1

print(fish_count)

for day in range(256):
    new_fish = np.zeros(9)
    for i in range(len(new_fish)):
        if i != 8:
            new_fish[i] = fish_count[i+1]

    new_fish[6] += fish_count[0]
    new_fish[8] += fish_count[0]

    fish_count = new_fish

print(sum(fish_count))



# current_fish = init_fish
# total_fish = current_fish
# for day in range(80):
#     print(day)
#
#     current_fish = total_fish
#     for fish in current_fish:
#         new_fish = current_fish - 1
#
#         baby_fish = []
#         for parent in range(len(new_fish)):
#             if new_fish[parent] == -1:
#                 new_fish[parent] = 6
#                 baby_fish.append(8)
#
#         total_fish = np.concatenate((new_fish, np.array(baby_fish)), axis=0)
#
# print(len(total_fish))



