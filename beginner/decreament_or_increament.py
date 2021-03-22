# PROBLEM: Decrement OR Increment


# STATEMENT:
# Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by 1.

# Input:
# First line will contain a number N.
# Output:
# Output a single line, the new value of the number.

# Constraints
# 0≤N≤1000
# Sample Input:
# 5
# Sample Output:
# 4


# SOLUTIONS:

# solution(1):
n = int(input())
print(n+1 if n%4 == 0 else n-1)

# solution(2):
print((lambda x:x+1 if x%4==0 else x-1)(int(input())))