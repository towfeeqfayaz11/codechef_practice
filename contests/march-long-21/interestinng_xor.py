# Problem: Interesting XOR!

# statement:
# You are given an integer C. Let d be the smallest integer such that 2d is strictly greater than C.

# Consider all pairs of non-negative integers (A,B) such that A,B<2d and A⊕B=C (⊕ denotes the bitwise XOR operation). Find the maximum value of A⋅B over all these pairs.

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains a single integer C.
# Output
# For each test case, print a single line containing one integer ― the maximum possible product A⋅B.

# Constraints
# 1≤T≤105
# 1≤C≤109
# Subtasks
# Subtask #1 (30 points): 1≤C≤103
# Subtask #2 (70 points): original constraints

# Example Input
# 2
# 13
# 10
# Example Output
# 70
# 91
# Explanation
# Example case 1: The binary representation of 13 is "1101". We can use A=10 ("1010" in binary) and B=7 ("0111" in binary). This gives us the product 70. 
# No other valid pair (A,B) can give us a larger product.

# Example case 2: The binary representation of 10 is "1010". We can use A=13 ("1101") and B=7 ("0111"). This gives us the maximum product 91.