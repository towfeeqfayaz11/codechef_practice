# Problem: Second Largest

# Statement: 
# Three numbers A, B and C are the inputs. Write a program to find second largest among them.

# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains three integers A, B and C.

# Output
# For each test case, display the second largest among A, B and C, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ A,B,C ≤ 1000000
# Example
# Input
# 3 
# 120 11 400
# 10213 312 10
# 10 3 450

# Output

# 120
# 312
# 10


# Solutions:

# solution(1):
for _ in range(int(input())):
    A,B,C = map(int, input().split())
    if A>B and B>C or C>B and B>A:
        print(B)
    elif B>C and C>A or A>C and C>B:
        print(C)
    else:
        print(A)




# solution(2):
for _ in range(int(input())):
    A,B,C = map(int, input().split())
    if A>=B>=C or C>=B>=A:
        print(B)
    elif B>=C>=A or A>=C>=B:
        print(C)
    else:
        print(A)




# solution(3):
for _ in range(int(input())):
    list1 = list(map(int,input().split()))
    list1.sort()
    print(list1[1])




# solution(4):
for _ in range(int(input())):
    list1 = sorted(list(map(int,input().split())))
    print(list1[1])
