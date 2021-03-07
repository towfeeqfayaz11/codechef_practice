# Problem: Finding Square Roots

# Statement:
# In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages .

# Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions. So here's your chance.

# Input
# The first line of the input contains an integer T, the number of test cases. T lines follow. Each line contains an integer N whose square root needs to be computed.

# Output
# For each line of the input, output the square root of the input integer, rounded down to the nearest integer, in a new line.

# Constraints
# 1<=T<=20
# 1<=N<=10000
# Input:
# 3
# 10
# 5
# 10000

# Output:
# 3
# 2
# 100


# Solutions:



# solution(1):
import math
for _ in range(int(input())):
    print(int(math.sqrt(int(input()))))



# solution(2):
for _ in range(int(input())):
    print(int((int(input()))**0.5))


# solution(3):
for _ in range(int(input())):
    print(round((int(input()))**0.5))


# solution(4):
for _ in range(int(input())):
    print(round((int(input()))**(1/2)))