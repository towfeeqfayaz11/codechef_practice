# problem: Mahasena

# Statement:
# Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, 
# and "unlucky" otherwise. He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" 
# soldiers, and "NOT READY" otherwise.

# Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".

# Note: You can find the definition of an even number here.

# Input
# The first line of input consists of a single integer N denoting the number of soldiers. The second line of input consists of N space separated 
# integers A1, A2, ..., AN, where Ai denotes the number of weapons that the ith soldier is holding.

# Output
# Generate one line output saying "READY FOR BATTLE", if the army satisfies the conditions that Kattapa requires or "NOT READY" otherwise (quotes for clarity).

# Constraints
# 1 ≤ N ≤ 100
# 1 ≤ Ai ≤ 100
# Example 1
# Input:
# 1
# 1

# Output:
# NOT READY
# Example 2
# Input:
# 1
# 2

# Output:
# READY FOR BATTLE
# Example 3
# Input:
# 4
# 11 12 13 14

# Output:
# NOT READY
# Example 4
# Input:
# 3
# 2 3 4

# Output:
# READY FOR BATTLE
# Example 5
# Input:
# 5
# 1 2 3 4 5

# Output:
# NOT READY

# Solutions:


# solution(1):
n = int(input())
w = list(map(int,input().split()))
c = 0
for i in w:
    if i & 1 == 0:
        c += 1
if c > n/2:
    print('READY FOR BATTLE')
else:
    print('NOT READY')



# solution(2): 
ns= int(input())
nw = list(map(int,input().split()))
ew = list(filter(lambda x: x%2==0,nw))
ow = list(filter(lambda x: x%2!=0,nw))
print("READY FOR BATTLE" if len(ew)>len(ow) else "NOT READY")



# solution(3):
n = int(input())
weapons = list(map(int, input().split()))
count = list(map(lambda x: x & 1, weapons)).count(0)
print('READY FOR BATTLE' if count > n/2 else 'NOT READY')


# solution(4):
n = int(input())
weapons = list(map(int, input().split()))
result = [1 for i in weapons if i & 1 == 0]
print('READY FOR BATTLE' if len(result) > n/2 else 'NOT READY')


# solution(5):
n = int(input())
weapons = list(map(int, input().split()))
tmp = [1] * n
result = [1 for a,b in zip(weapons,tmp) if a & b == 0]
print('READY FOR BATTLE' if len(result) > n/2 else 'NOT READY')