# Problem: Enormous Input Test

# Statement:
# The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded 
# with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.

# Input
# The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.

# Output
# Write a single integer to output, denoting how many integers ti are divisible by k.

# Example
# Input:
# 7 3
# 1
# 51
# 966369
# 7
# 9
# 999996
# 11

# Output:
# 4


# Solutions:

# solution(1):    # this code runs slow as while loop is slow compare to for because of range
                  # for loop with range is faster than while loop with increament
                  # because there is a lot of object creation and destruction going on with the while looop (e.g; i += 1)
n,k = map(int,input().split())
res = 0
while n:
    t = int(input())
    if t%k == 0:
        res += 1
    n -= 1
print(res)





# solution(2): (this is faster than above code)
n,k = map(int,input().split())
res = 0
# for loop with range is faster than while loop with increament
# because there is a lot of object creation and destruction going on with the while loop
for i in range(n):         
    t = int(input())       
    if t%k == 0:
        res += 1
print(res)





# solution(3):
(n, k) = map(int, input().split(' '))
ans = 0
for i in range(n):
	x = int(input())
	if x % k == 0:
		ans += 1
print(ans)