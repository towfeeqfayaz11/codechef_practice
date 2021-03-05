# Problem: Turbo Sort

# Statement:
# Given the list of numbers, you are to sort them in non decreasing order.
# Input
# t – the number of numbers in list, then t lines follow [t <= 10^6].
# Each line contains one integer: N [0 <= N <= 10^6]

# Output
# Output given numbers in non decreasing order.
# Example
# Input:

# 5
# 5
# 3
# 6
# 7
# 1
# Output:

# 1
# 3
# 5
# 6
# 7


# Solutions:


# solution(1):
mylist = [] # creating emptylist
for _ in range(int(input())):
    mylist.append(int(input()))
    
mylist.sort()    # list.sort() is faster than python's sorted()

for N in mylist:
    print(N)
    
# list.sort() has return type as none 
# (it does inplace sort thus return none like all inplace operations)
# sorted(list) --> returns the sorted list



# solution(2):
mylist = [] # creating emptylist
for _ in range(int(input())):
    mylist.append(int(input()))
    
for N in sorted(mylist):
    print(N)