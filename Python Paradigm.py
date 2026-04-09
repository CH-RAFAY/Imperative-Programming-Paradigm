# Reversing string

S = "TypicalString"
print(S)

def reverse_string(S):
    return S[::-1]

print(reverse_string(S))




# Method 1: Slicing (Most Pythonic - One Liner)
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print(reversed_arr)




# Check Duplication of Array

my_list = [1, 2, 5, 6, 3, 4, 5, 2, 6]
seen = set()
duplications = []

for x in my_list:
    if x in seen:
        duplications.append(x)
    else:
        seen.add(x)

print (duplications)





#Finding Second Largest element in an array
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

def second_largest(arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

print(second_largest(arr))


#Count frequency of characters

from collections import Counter
s = "hello world"

def freq(s):
    return Counter(s)

print(freq(s))




from collections import Counter

def freq(s):
    return Counter(s)

    s = int(input())
def is_prime(s):
    if s<2:
        return False
    if (s**0.5+1%2 == 0):
        return True
        
print(is_prime())

name = input("What is your name? ")
print(f"Hello, {name}! Welcome to Python.")


import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
password = "".join(random.choice(chars) for _ in range(12))
print(f"Generated Password: {password}")


def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("radar"))  # Returns: True
