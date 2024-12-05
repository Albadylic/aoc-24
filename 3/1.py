from input import input
import re

multiplyregex = 'mul\(\d{1,3},\d{1,3}\)'
doregex = 'do\(\)'
dontregex = "don\'t\(\)"

# Split the original string on every time that 'do()' occurs
domatches = re.split(doregex, input)

# Split the list by don't()'s
def splitthematches(el):
    return re.split(dontregex, el)
splitbydont = list(map(splitthematches, domatches))

# Delete every second item, to ignore the cases with 'dont'
del splitbydont[1::2]

# Join the lists into a string
def joinlist(arr):
    return ''.join(arr)
newinput = ''.join(list(map(joinlist, splitbydont)))

# Do what we did in part 1
matches = re.findall(multiplyregex, newinput)

def removefluff(el):
    pair = re.split(',', re.sub("\)", '', re.sub("mul\(",'', el)))
    return pair

def multiply(pair):
    return int(pair[0]) * int(pair[1])

result = sum(list(map(multiply, map(removefluff, matches))))

print(result)

# 79233424 is too low
# 81852502 is too low