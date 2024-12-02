from input import input

def formatinput (str):
    rows = str.splitlines()
    def splitRows(row):
        return row.split("   ")
    pairs = list(map(splitRows, rows))

    leftList = []
    rightList = []
    for pair in pairs:
        leftList.append(int(pair[0]))
        rightList.append(int(pair[1]))

    leftList.sort()
    rightList.sort()
    return [leftList, rightList]

def calculateDistance (list):
    total = 0
    i = 0
    for i in range(len(list[0])):
        dist = list[0][i] - list[1][i]
        if dist < 0:
            total += -1 * dist
        else:
            total += dist
    return total

# print(calculateDistance(formatinput(input)))

def countOccurences(list):
    total = 0
    i = 0
    for i in range(len(list[0])):
        occurences = list[1].count(list[0][i])
        total += list[0][i] * occurences
    return total

print(countOccurences(formatinput(input)))