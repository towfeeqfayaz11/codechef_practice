# Problem: Sum of Digits

# Statement:
# You're given an integer N. Write a program to calculate the sum of all the digits of N.

# Input
# The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, calculate the sum of digits of N, and display it in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 3 
# 12345
# 31203
# 2123
# Output
# 15
# 9
# 8

# Solutions:

# solution(1):
T = int(input())

for tc in range(T):
    N = input()
    res = 0
    for i in N:
        res += int(i)
    print(res)




# solution(2):
T = int(input())

for tc in range(T):
    sum = 0 
    N = int(input())
    while(N):
        sum = sum + int(N % 10)
        N = int(N/10)
    print(sum)



# solution(3):
t=int(input())
for i in range(t):
    x = int(input())
    sum1=0
    while x>0:
        rem =x%10
        sum1=sum1+rem
        x=x//10                 # not used int method here
    print(sum1)


 # solution(4):
 t=int(input())
for i in range(t):
    m=input()
    x=[int(i) for i in m]  # list comprehension
    print(sum(x))
