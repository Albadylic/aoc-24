from input import input
import re

multiplyregex = 'mul\(\d{1,3},\d{1,3}\)'
doregex = 'do\(\)'
dontregex = "don\'t\(\)"


domatches = re.split(doregex, input)

def splitthematches(el):
    return re.split(dontregex, el)

splitbydont = list(map(splitthematches, domatches))
del splitbydont[1::2]
def joinlist(arr):
    return ''.join(arr)
newinput = ''.join(list(map(joinlist, splitbydont)))
matches = re.findall(multiplyregex, newinput)

def removefluff(el):
    pair = re.split(',', re.sub("\)", '', re.sub("mul\(",'', el)))
    return pair

def multiply(pair):
    return int(pair[0]) * int(pair[1])

result = sum(list(map(multiply, map(removefluff, matches))))

print(result)

# 79233424 is too low