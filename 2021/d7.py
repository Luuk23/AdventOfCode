import numpy as np

with open("inputd7.txt") as file:
    crabs = np.array([int(n) for n in file.readline().split(",")])
    print(crabs)

median_crab = int(np.median(crabs))
print(median_crab)

fuel = []
for ii in range(min(crabs), max(crabs)):
    fuel_sum = 0
    for pos in crabs:
        fuel_sum += sum(range(abs(pos - ii)+1))
    if fuel_sum > 0:
        fuel.append(fuel_sum)

print(fuel)
print(min(fuel))
