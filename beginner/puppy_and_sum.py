# Problem: Puppy and Sum

# statement:
# Yesterday, puppy Tuzik learned a magically efficient method to find the sum of the integers from 1 to N. He denotes it as sum(N). But today, as a true explorer, 
# he defined his own new function: sum(D, N), which means the operation sum applied D times: the first time to N, and each subsequent time to the result of the 
# previous operation.

# For example, if D = 2 and N = 3, then sum(2, 3) equals to sum(sum(3)) = sum(1 + 2 + 3) = sum(6) = 21.

# Tuzik wants to calculate some values of the sum(D, N) function. Will you help him with that?

# Input
# The first line contains a single integer T, the number of test cases. Each test case is described by a single line containing two integers D and N.

# Output
# For each testcase, output one integer on a separate line.

# Constraints
# 1 ≤ T ≤ 16
# 1 ≤ D, N ≤ 4
# Example
# Input:
# 2
# 1 4
# 2 3

# Output:
# 10
# 21
# Explanation:
# The first test case: sum(1, 4) = sum(4) = 1 + 2 + 3 + 4 = 10.

# The second test case: sum(2, 3) = sum(sum(3)) = sum(1 + 2 + 3) = sum(6) = 1 + 2 + 3 + 4 + 5 + 6 = 21.


# solutions:


# solution(1):
for _ in range(int(input())):
    D,N = map(int, input().split())
    for _ in range(D):
        N = N*(N+1)//2    #sum of first n natural numbers
    print(N)



# solution(2):
for _ in range(int(input())):
    D,N = map(int, input().split())
    for _ in range(D):
        N = sum(range(N+1))
    print(N)