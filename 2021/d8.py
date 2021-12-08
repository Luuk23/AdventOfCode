with open("inputd8.txt") as file:
    patterns = [p.split(" | ")[1].split() for p in [n for n in file.read().splitlines()]]
    print(patterns)

part1 = [item for sublist in patterns for item in sublist if len(item) in [2,3,4,7]]
print(len(part1))


with open("inputd8.txt") as file:
    inputs = [p.split(" | ")[0].split() for p in [n for n in file.read().splitlines()]]
    print(inputs)

with open("inputd8.txt") as file:
    outputs = [p.split(" | ")[1].split() for p in [n for n in file.read().splitlines()]]
    print(outputs)


def get_key(val, decoder):
    for key, value in decoder.items():
        if val == value:
            return key


def decode_069(one, eight, target, decoder):
    if one[0] not in target:  # then target == 6
        decoder[one[0]] = 'c'
        decoder[one[1]] = 'f'
    elif one[1] not in target:  # then target == 6
        decoder[one[1]] = 'c'
        decoder[one[0]] = 'f'
    else:
        for n in eight:
            if n not in target:
                indic = n

        temp = get_key('eg', decoder)
        if indic in temp: # then target == 9
            if temp[0] not in target:
                decoder[temp[0]] = 'e'
                decoder[temp[1]] = 'g'
            elif temp[1] not in target:
                decoder[temp[1]] = 'e'
                decoder[temp[0]] = 'g'
        else: # then target == 0
            temp2 = get_key('bd', decoder)
            decoder[indic] = 'd'
            for t in temp2:
                if t != indic:
                    decoder[t] = 'b'


general_decoder = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf': 4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8,
                   'abcdfg': 9}
all_decoders = []
for ii in inputs:
    ii.sort(key=len)
    ii = [''.join(sorted(s)) for s in ii]

    decoder = {}

    # decode 1
    decoder[ii[0]] = 'cf'

    # decode 7
    for jj in ii[1]:
        if jj not in ii[0]:
            decoder[jj] = 'a'

    # decode 4
    temp = ""
    for jj in ii[2]:
        if jj not in ii[0]:
            temp += jj
    decoder[temp] = 'bd'

    # decode 8
    temp = ""
    for jj in ii[-1]:
        if jj not in ii[0] and jj not in ii[1] and jj not in ii[2]:
            temp += jj
    decoder[temp] = 'eg'

    # decode 0/6/9
    decode_069(ii[0], ii[-1], ii[-2], decoder)
    decode_069(ii[0], ii[-1], ii[-3], decoder)
    decode_069(ii[0], ii[-1], ii[-4], decoder)

    all_decoders.append(decoder)

summation = 0
for ii in range(len(outputs)):
    number = ""
    for outp in outputs[ii]:
        decoded = ''
        for n in outp:
            decoded += all_decoders[ii][n]
        decoded = "". join(sorted(decoded))
        number += str(general_decoder[decoded])

    summation += int(number)

print(summation)