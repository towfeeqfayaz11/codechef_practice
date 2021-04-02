# Problem: GCD and LCM

# NOTE: 

# GCD or HCF --> Largest Integer that can divide both the numbers without any remainder or with 0 as remainder.
# LCM        --> is the smallest positive integer that is perfectly divisible by the given integer values.

# LCM * HCF = product of two numbers
# ------------------------------------------------------
# => different ways to find gcd/hcf efficiently using euclid's algorithm
# euclid's algo has  two cases
  #1> gcd(a,b) = gcd (b,a%b) -->this approach makes sure automatically that a > b (you don't need to worry about that)  --> can be done  using either recurssion or iteration
  #2> base case: gcd(a,0) = a

  Method1: recurssion
  def find_gcd (a,b):
  	if b==0:             # base case
  	  return a
  	return (b,a%b)

  Method2: using iteration
  def find_gcd(a,b):
  	while(b):
  		a,b = b, a%b
  	return a

  Method3: recurssion
  def gcd(a,b):
     
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)




# -----------------------------------------------------





# Statement:
# Two integers A and B are the inputs. Write a program to find GCD and LCM of A and B.

# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer A and B.

# Output
# Display the GCD and LCM of A and B separated by space respectively. The answer for each test case must be displayed in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# 1 ≤ A,B ≤ 1000000
# Example
# Input
# 3 
# 120 140
# 10213 312
# 10 30

# Output

# 20 840
# 1 3186456
# 10 30



# solutions:


# solution(1):
from sys import stdin
for _ in range(int(input())):
    A,B = map(int, stdin.readline().split())
    n1,n2 = A,B
    # finding hcf using euclids algorithm
    while (n1 != n2):         # to find hcf
        if n1>n2:
            n1 = n1-n2
        else:
            n2 = n2-n1
    print(n1,(A*B)//n1)           # n1 is hcf or gcd and A*B//n1 is lcm


# from sys import stdin
# for _ in range(int(stdin.readline())):
#     A,B = map(int, stdin.readline().split())
#     for i in range(1, min(A,B)+1):
#         if A%i == 0 and B%i == 0:
#             hcf = i
#     lcm = (A*B) // hcf
#     print(hcf,lcm)





# from sys import stdin
# for _ in range(int(stdin.readline())):
#     A,B = map(int, stdin.readline().split())
#     lcm = max(A,B)
#     m = lcm
#     while (lcm % A !=0 or lcm % B !=0):
#         lcm += m
#     hcf = (A*B)//lcm
#     print(hcf,lcm)




# solution(2):
for _ in range(int(input())):
    A,B = map(int, input().split())
    n1,n2 = A,B
    while(n2):
        n1,n2 = n2, n1%n2
    print(n1,A*B//n1)



# solution(3):
def find_gcd(n1,n2):
    if n2==0:
        return n1
    return find_gcd(n2,n1%n2)
    
for _ in range(int(input())):
    A,B = map(int, input().split())
    hcf=find_gcd(A,B)
    print(hcf, A*B//hcf)
