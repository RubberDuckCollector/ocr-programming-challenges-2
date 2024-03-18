# ocr-programming-challenges-2

https://www.ocr.org.uk/Images/260930-coding-challenges-booklet.pdf

## Challenges completed:

<!-- vim-markdown-toc GFM -->

* [1 - Factorial Finder](#1---factorial-finder)
* [3 - Thief!](#3---thief)
* [2 - Speed Tracker](#2---speed-tracker)
* [5 - Fruit Machine](#5---fruit-machine)
* [6 - Unit Converter](#6---unit-converter)
* [8 - Arithmetic Test](#8---arithmetic-test)
* [9 - Happy Numbers](#9---happy-numbers)
* [12 - Quiz Maker](#12---quiz-maker)
* [15 - Pangrams](#15---pangrams)
* [20 - Palindromes](#20---palindromes)
* [22 - Simple Life Calculator](#22---simple-life-calculator)
* [23 - Fibbing](#23---fibbing)
* [24 - Hack Proof](#24---hack-proof)
* [25 - Ordering](#25---ordering)
* [30 - Year Addition](#30---year-addition)
* [31 - Forwards and Backwards](#31---forwards-and-backwards)
* [33 - Mor-se Coding](#33---mor-se-coding)
* [34 - What's the day?](#34---whats-the-day)
* [36 - Triangulate (WIP)](#36---triangulate-wip)
* [37 - Fizz Buzz](#37---fizz-buzz)
* [38 - Sing along](#38---sing-along)
* [39 - Even more Odd](#39---even-more-odd)
* [40 - Base of Numbers](#40---base-of-numbers)
* [41 - Prime Factorisation](#41---prime-factorisation)
* [45 - Find the factorial](#45---find-the-factorial)
* [48 - Reverse It](#48---reverse-it)
* [61 - Your name is...](#61---your-name-is)
* [62 - R@nd0m-P@ssw0rd--generator](#62---rnd0m-pssw0rd--generator)
* [63 - I like P](#63---i-like-p)
* [76 - That's a lot of number](#76---thats-a-lot-of-number)
* [77 - Fib on a chi](#77---fib-on-a-chi)

<!-- vim-markdown-toc -->

### 1 - Factorial Finder

Easy

### 3 - Thief!

It's very easy with `itertools.perumations()` it returns an itertools object that you can cast into a list and it will be a list of tuples of the permutations

### 2 - Speed Tracker

I don't even know what was going on

### 5 - Fruit Machine

This had some if statements I needed to get my head around which took a long time, but overall it wasn't too bad with the exception of the money part. Figuring out when to subtract or add on money to the user's balance was difficult and I resorted to trial and error. The fruit machine had some very difficult sequence for my level when and how I completed it

### 6 - Unit Converter

The unit converter wasn't too hard. I just had to make sure to keep my code reasonably modular by pre-defining functions that return the converted units so I could call them when the user is prompted for an input

### 8 - Arithmetic Test

This was pretty easy. I wrote repetitive code but it doesn't really matter for me. I did extension 1 but not extension 2 because extension 2 was too hard for me

### 9 - Happy Numbers

I figured out how to determine a happy number very quickly, and then got stuck trying to use a for loop to test many numbers to see if they're a happy number or not. That took me a very long time and I couldn't do it. All of my attempts were long winded and never going to work

```Python
def find_happy_numbers(b):
    happy_list = []
    count = 0

    while b not in happy_list and count < 50:
        happy_list.append(b)
        b = happy_numbers(b)
        count += 1
    return b == 1
```

### 12 - Quiz Maker

This was easy for me. The only tricky parts are reading the questions and answers from the file in the correct way (as sublists in a bigger list) and correctly processing each element in the sublists with the list comprehension

### 15 - Pangrams

This was quite easy for me because brute forcing it is easy.

### 20 - Palindromes

Palindromes in Python are very easy. There are 2 shorthand techniques where:

```Python
message = message[::-1] # reverses the string

return msg[::-1] == msg # this will return either True or False due to the "=="
```

### 22 - Simple Life Calculator

Too real

### 23 - Fibbing

This was pretty easy for me. I remmebered the recursive solustion to the fibonacci sequence so I used that and the rest was knowledge of for loops and the builtin `reversed` and `sum` keywords

### 24 - Hack Proof

Pretty easy

### 25 - Ordering

This wasn't hard other than `msg = "".join([i for i in msg])` which converts the list into a string while joining each element with the data in quotes

### 30 - Year Addition

Easy

### 31 - Forwards and Backwards

I think it's the same as number 20

### 33 - Mor-se Coding

Challenge 33 was definitely hard. I found decoding morse code to be much harder than encoding. This was a fun challenge and it's one of the more practical ones I've tried.

### 34 - What's the day?

Easy with the datetime library

### 36 - Triangulate (WIP)

I used the internet to learn about the triangle inequality theorem so I could complete the non-extension part of the challenge. I then re-learned the sine rule to help me figure out how to do the extension, but coming up with solutions confused me so I left the extension for later

### 37 - Fizz Buzz

Easy

### 38 - Sing along

This is very easy in python if you know the reversed for loop

### 39 - Even more Odd

Pretty fun if you use list comprehension to make the odd and even lists in this way of doing it

```Python
even = [i for i in nums if i % 2 == 0]
odd = [i for i in nums if i % 2 != 0]
```

### 40 - Base of Numbers

This has very simple but effective solutions

### 41 - Prime Factorisation

I tried to do something crazy until I went crazy and I used the internet
The comments in the `prime_factors` function are a graveyard

### 45 - Find the factorial

Easy and also the same as challenge 1

### 48 - Reverse It

Again quite an easy challenge, all you need to do is iterate through the vowels and consonants and also remember the shorthand for reversing a string:

```Python
msg = msg[::-1] # string slicing syntax

msg = "".join(reversed(msg)) # this also works somehow
```

### 61 - Your name is...

Easy

### 62 - R@nd0m-P@ssw0rd--generator

Easy

### 63 - I like P

Easy

### 76 - That's a lot of number

Very interesting list comprehension involving a file read and casting

```Python
nums = [int(i) for i in f]
```

### 77 - Fib on a chi

I'm guessing there is a way to calculate the answer but I did it empirically because it's easy and answers the question
