from input import input

# Split lines, split each line, convert each str to int
def formatinput(str):
    reports = str.splitlines()
    for i in range(len(reports)):
        reports[i] = reports[i].split(" ")
        for j in range(len(reports[i])):
            reports[i][j] = int(reports[i][j])
    return reports

def checkValues(list, str, run):
    # Introduce a factor which is set to -1 when the list is increasing
    # Otherwise, it's 1
    factor = 1
    if (str == 'inc'):
        factor =  -1

    index = 0
    for index in range(len(list)):
        # Break when the index is the last value
        if (index == len(list) - 1):
            return True
        diff = (list[index] - list[index + 1]) * factor
        if diff > 3 or diff < 1:
            if run == 1:
                return False
            else:
                # Pass the list to the dampener with the problem val removed
                del list[index]
                return checkValues(list, str, 1)

def checkDifferences(list):
    differences = []
    for i in range(len(list) - 1):
        diff = list[i] - list[i + 1]
        differences.append(diff)
    countsafe = 0
    for i in range(len(differences)):
        if 1<= differences[i] <= 3:
            countsafe += 1
        elif -1 >= differences[i] >= -3:
            countsafe -= 1

    if abs(countsafe) == len(list) - 1 or abs(countsafe) == len(list) + 1:
        # print(f"list: {len(list)}, countsafe: {countsafe}")
        return True
    elif abs(countsafe) == len(list) - 2 or abs(countsafe) == len(list) + 2:
        # print(f"list: {len(list)}, countsafe: {countsafe}")
        return True
    else:
        # if (len{list})
        print(f"list: {len(list)}, countsafe: {countsafe}")
        return False

    # Countsafe can be equal to the length of the list
    # or it can be one less than the length


def checkLevel(list):
    i = 0
    output = []
    outcome = False
    for i in range(len(list)):
        outcome = checkDifferences(list[i])
        if (outcome == True):
            output.append(list[i])
    return len(output)


print(checkLevel(formatinput(input)))
