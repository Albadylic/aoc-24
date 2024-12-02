from input import input

# Split lines, split each line, convert each str to int
def formatinput(str):
    reports = str.splitlines()
    for i in range(len(reports)):
        reports[i] = reports[i].split(" ")
        for j in range(len(reports[i])):
            reports[i][j] = int(reports[i][j])
    return reports

def checkDecreasing(list):
    index = 0
    for index in range(len(list)):
        diff = list[index] - list[index + 1]
        if diff > 3 or diff < 1:
            return False

def checkIncreasing(list):
    index = 0
    for index in range(len(list)):
        # For increasing, the difference will be negative
        # i.e. 6 - 7 = -1
        # Multiply by -1 to check the pattern is correct
        diff = (list[index] - list[index + 1]) * -1
        if diff > 3 or diff < 1:
            return False


def checkLevel(list):
    i = 0
    output = []
    outcome = False
    for i in range(len(list)):
        for j in range(len(list[i])):
            difference = list[i][j] - list[i][j]
            if difference > 0:
                # Send out to another function to check specifics
                # Return T / F
                outcome = checkDecreasing(list[i])
            elif difference < 1:
                outcome = checkIncreasing(list[i])
            else:
                # Handle cases with no difference 
                outcome = False
        if (outcome == True):
            output.append(list[i])
    return len(output)


print(checkLevel(formatinput(input)))
