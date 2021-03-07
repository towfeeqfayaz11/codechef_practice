# Problem: Reverse The Number

# Statement:
# Given an Integer N, write a program to reverse it.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

# Output
# For each test case, display the reverse of the given number N, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ N ≤ 1000000
# Example
# Input
# 4
# 12345
# 31203
# 2123
# 2300
# Output
# 54321
# 30213
# 3212
# 32


# Solutions:


# solution(1):                  # pythonic way
for _ in range(int(input())):
    print(int(input()[::-1]))


# solution(2):                   general way
for _ in range(int(input())):
    N = int(input())
    rev = 0
    while N > 0:
        rev = rev * 10 + N % 10
        N = N // 10
    print(rev)

