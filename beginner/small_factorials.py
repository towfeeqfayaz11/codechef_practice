# Problem: Small factorials



# Statement:

# You are asked to calculate factorials of some small positive integers.

# Input
# An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1<=n<=100.

# Output
# For each integer n given at input, display a line with the value of n!

# Example
# Sample input:
# 4
# 1
# 2
# 5
# 3
# Sample output:

# 1
# 2
# 120
# 6


# Solutions:


# solution(1):
def find_factorial(n):
    if n == 0 or n==1:
        return 1
    small_ans = find_factorial(n-1)
    return n * small_ans
for _ in range(int(input())):
    print(find_factorial(int(input())))




# solution(2):
for _ in range(int(input())):
    n = int(input())
    fact = 1
    for i in range(1, n+1):
        fact *= i
        
    print(fact)
    

# solution(3):
import math

n=int(input())
for x in range(n):
    i=int(input())




# solution(4):
try:
    def factorial(n):
        i = 1
        while n>0:
            i = i*(n)
            n = n-1
        print(i)
    #main
    t = int(input())
    for _ in range(t):
        n = int(input())
        factorial(n)
except:
    pass
    print(math.factorial(i))