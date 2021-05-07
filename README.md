## Programming exercises

Used to quickly catch up with a new programming language

## Exercises

1. Define a function halve :: [a] -> ([a],[a]) that splits an even-lengthed list into two halves.

2. Define a function third :: [a] -> a that returns the third element in a list that contains at least this many elements

3. The Luhn algorithm is used to check bank card numbers for simple errors such as mistyping a digit, and proceeds as follows:

- consider each digit as a separate number;
- moving left, double every other number from the second last;
- subtract 9 from each number that is now greater than 9;
- add all the resulting numbers together;
- if the total is divisible by 10, the card number is valid.
