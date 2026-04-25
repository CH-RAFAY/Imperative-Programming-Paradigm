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









def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(f"25°C is {celsius_to_fahrenheit(25)}°F")





# Simple addition tool
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 + num2

print(f"The sum of {num1} and {num2} is {result}")


# A simple countdown timer
count = 5

while count > 0:
    print(count)
    count -= 1  # Subtract 1 from count each time

print("Blast off!")


fizzbuzz = ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else i for i in range(1, 16)]
print(fizzbuzz)


text = "complexity"
char_counts = {char: text.count(char) for char in set(text)}
print(char_counts)



# Variables
name = "Python"
version = 3.12

# Simple Math
a = 10
b = 5
print(f"Sum of {a} and {b} is {a + b}")


# Prints 1, 2, 3... up to 10
for i in range(1, 11):
    print(i)



import uuid

# Generate a random unique ID (UUID4)
unique_id = uuid.uuid4()

print(f"Full UUID: {unique_id}")
print(f"Hex format: {unique_id.hex}")





name = "Alice"
age = 25
next_year = age + 1

print(f"Hi {name}, next year you will be {next_year}!")



def get_perms(s):
    if len(s) <= 1: return [s]
    res = []
    for i in range(len(s)):
        res += [p[:i] + [s[0]] + p[i:] for p in get_perms(s[1:])]
    return res
def get_primes(n):
    primes = [True] * (n + 1)
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            primes[p*p : n+1 : p] = [False] * len(range(p*p, n+1, p))
    return [i for i in range(2, n + 1) if primes[i]]
