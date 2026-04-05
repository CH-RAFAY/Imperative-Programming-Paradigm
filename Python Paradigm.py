# Reversing string

S = "TypicalString"
print(S)

def reverse_string(S):
    return S[::-1]

print(reverse_string(S))




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



# Method 1: Slicing (Most Pythonic - One Liner)
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print(reversed_arr)  # [5, 4, 3, 2, 1]

