# Problem: Small Factorial

# Statement: 
# Write a program to find the factorial value of any number entered by the user.

# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains an integer N.

# Output
# For each test case, display the factorial of the given number N in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 0 ≤ N ≤ 20
# Example
# Input
# 3 
# 3 
# 4
# 5

# Output

# 6
# 24
# 120


# Solutions:


# solution(1):
for _ in range(int(input())):
    res = 1
    for i in range(2,int(input())+1):
        res*=i
    print(res)


# solution(2):
def find_factorial(fact):
    if fact ==0 or fact ==1:
        return 1
    small_fact = find_factorial(fact-1)
    return fact * small_fact
    
for _ in range(int(input())):
    print(find_factorial(int(input())))


# solution(3):
import math

n=int(input())

while n>0 :
    m=int(input())
    print(math.factorial(m))
    n=n-1