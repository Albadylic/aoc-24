from input import input
import re

regex = 'mul\(\d{1,3},\d{1,3}\)'

matches = re.findall(regex, input)

def removefluff(el):
    pair = re.split(',', re.sub("\)", '', re.sub("mul\(",'', el)))
    return pair

def multiply(pair):
    return int(pair[0]) * int(pair[1])

result = sum(list(map(multiply, map(removefluff, matches))))

print(result)