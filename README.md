![Dart CI status](https://github.com/zinh/programming_exercises/actions/workflows/dart.yml/badge.svg)
![Dart CI status](https://github.com/zinh/programming_exercises/actions/workflows/python.yml/badge.svg)

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

4. Calculates the sum 1^2 + 2^2 + ... 100^2 of the first one hundred integer squares.

5. Implement `replicate`, eg: `replicate 3 true = [true, true, true]`

6. Write function that returns all Pythagorean whose components are at most a given limit.

7. A positive integer is perfect if it equals the sum of all of its factors, excluding the number itself.
Write a function that returns the list of all perfect numbers up to a given limit.

8. Write a function that returns dot production of two vectors.

9. Define a recursive function `euclid :: Int -> Int -> Int `
that implements Euclid’s algorithm for calculating the greatest common divisor of two non-negative integers: 
if the two numbers are equal, this number is the result; otherwise, the smaller number is subtracted from the larger,
and the same process is then repeated.

10. Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

10. Implement merge sort

11. Define `dec2int :: [Int] -> Int` using fold. Eg: `dec2int [2 3 4 5] = 2345`

12. Implement `unfold`, where:

```haskell
unfold p h t x | p x = []
               | otherwise = h x : unfold p h t (t x)
```

Use unfold to implement:

- int2bin
- map f
- iterate f

13. Define `altMap :: (a -> b) -> (a -> b) -> [a] -> [b]`, eg:

```haskell
altMap (+10) (+100) [0,1,2,3,4] = [10,101,12,103,14]
```

14. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

15. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

14. The countdown problem

Given a sequence of numbers and a target number, attempt to construct an expression whose value is the target,
by combining one or more numbers from the sequence using addition, subtraction, multiplication, division and parentheses.

Each number in the sequence can only be used at most once in the expression, and all of the numbers involved,
including intermediate values, must be positive natural numbers (1, 2, 3, . . .).
In particular, the use of negative numbers, zero, and proper fractions such as 2 ÷ 3, is not permitted.

15. Implement Game of life

The game models a simple evolutionary system based on cells, and is played on a two-dimensional board. Each square on the board is either empty, or contains a single living cell.
Each internal square on the board has eight immediate neighbours.

Given an initial configuration of the board, the next generation of the board is given by simultaneously applying the following rules to all squares:

- a living cell survives if it has precisely two or three neighbouring squares that contain living cells, and
- an empty square gives birth to a living cell if it has precisely three neighbours that contain living cells, and remains empty otherwise.

16. Write a calculator that receive an expression(allow operations: +, -, \*, /, parenthesis) and calculate the result.
Extends to other operators: exponentation, logarithm, trigonometry functions.
