# Problem: primality Test

# statement:
# Alice and Bob are meeting after a long time. As usual they love to play some math games. This times Alice takes the call and decides the game. 
# e game is very simple, Alice says out an integer and Bob has to say whether the number is prime or not. Bob as usual knows the logic but 
# since Alice doesn't give Bob much time to think, so Bob decides to write a computer program.

# Help Bob accomplish this task by writing a computer program which will calculate whether the number is prime or not .

# Input
# The first line of the input contains an integer T, the number of testcases. T lines follow.

# Each of the next T lines contains an integer N which has to be tested for primality.

# Output
# For each test case output in a separate line, "yes" if the number is prime else "no."

# Constraints
# 1 ≤ T ≤ 20
# 1 ≤ N ≤ 100000
# Input:
# 5
# 23
# 13
# 20
# 1000
# 99991

# Output:
# yes
# yes
# no
# no
# yes


# Solutions:


# solution(1):
for _ in range(int(input())):
    n = int(input())
    if n <= 1:
        print('no')
    else:
        for i in range(2,n):
            if n % i == 0:
                print('no')
                break
        else:
            print('yes')



# solution(2):
import math
for _ in range(int(input())):
    n = int(input())
    if n <= 1:
        print('no')
    else:
        for i in range(2, n//2):
            if n % i == 0:
                print('no')
                break
        else:
            print('yes')



# solution(3):
import math
for _ in range(int(input())):
    n = int(input())
    if n <= 1:
        print('no')
    elif n == 2:
        print('yes')
    else:
        for i in range(3, (int(n//2))+1, 2):
            if n % i == 0:
                print('no')
                break
        else:
            print('yes')



# solution(4):
import math
for _ in range(int(input())):
    n = int(input())
    if n <= 1:
        print('no')
    else:
        for i in range(2,int(math.sqrt(n)) +1):
            if n % i == 0:
                print('no')
                break
        else:
            print('yes')


# solution(5)
import math
for _ in range(int(input())):
    n = int(input())
    if n <= 1:
        print('no')
    elif n == 2:
        print('yes')
    elif n > 2 and n%2 == 0:
        print('no')
    else:
        max_div = math.floor(math.sqrt(n))
        for i in range(3,max_div+1, 2):
            if n % i == 0:
                print('no')
                break
        else:
            print('yes')



# solution(6):
def isprime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print('yes' if isprime(n) else 'no')

