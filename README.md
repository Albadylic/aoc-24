# Advent of Code '24

This year, I'm using python for Advent of Code to improve my skills using the language and gain deeper familiarity with syntax and methods.

Here, I document learnings throughout the month.

## TIL

### 1/12

- `splitlines()` is a handy method for splitting each new line in an input
- `len(arr)` in py === `arr.length` in js
- for loops do not allow for an index while iterating. Instead, use an external variable which iterates alongside the length of the thing you're iterating through.

### 2/12

This one was fairly straighforward for part one but I got seriously lost in the weeds in part two.

Adapting my solution to work for inputs with one out of place number seemed straightforward but an initial misunderstanding lead me down a rabbithole. My initial solution was to allow cases where the `countsafe` count was an additional one more or less than the previously allowed value.

However, we needed instead to delete an index and then check. My first attempt was to try deleting each value and then calling the function again. This level of recursion however, sent in the list with values removed until only one value existed and every input returned true.

Back to the drawing board...

### 3/12

Exercise one was a fun opportunity to play with regex and learn about the functions available in python with regex.

I was able to use three of the four available functions:

1. `findall()` to search for all occurences of the required string
1. `sub()` allowed me to remove the _fluff_ from the strings which matched, i.e. the `mul(` and final closing bracket. I subbed these with an empty string to remove.
1. `split()` to split the number around the comma to get the two parameters

I then used the inbuilt sum function to add all the numbers after multiplying them.

My final line is a wee bit of a whacky one liner which sums and completes a double map 🤪
