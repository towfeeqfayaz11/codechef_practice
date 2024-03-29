# problem: The Block Game

# statement:
# The citizens of Byteland regularly play a game. They have blocks each denoting some integer from 0 to 9. These are arranged together in a random manner 
# without seeing to form different numbers keeping in mind that the first block is never a 0. Once they form a number they read in the reverse order to 
# check if the number and its reverse is the same. If both are same then the player wins. We call such numbers palindrome.

# Ash happens to see this game and wants to simulate the same in the computer. As the first step he wants to take an input from the user and check if the 
# number is a palindrome and declare if the user wins or not. 

# Input
# The first line of the input contains T, the number of test cases. This is followed by T lines containing an integer N.

# Output
# For each input output "wins" if the number is a palindrome and "loses" if not, in a new line.

# Constraints
# 1<=T<=20
# 1<=N<=20000
# Input:
# 3
# 331
# 666
# 343

# Output:
# loses
# wins
# wins



# solutions:

# solution(1):
for _ in range(int(input())):
    original_no = int(input())
    tmp = original_no
    new_no = 0
    while tmp !=0 :
        new_no = (10 * new_no) + (tmp % 10)
        tmp = tmp // 10
    if new_no == original_no:
        print('wins')
    else:
        print('loses')

# solution(2):
for _  in range(int(input())):
    n = input()
    print('wins' if n == n[::-1] else 'loses')

# solution(3):
for _  in range(int(input())):
    print((lambda n:'wins' if n == n[::-1] else 'loses') (input()))