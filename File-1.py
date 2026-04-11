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
