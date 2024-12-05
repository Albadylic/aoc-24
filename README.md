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
