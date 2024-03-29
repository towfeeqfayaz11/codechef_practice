# Problem: Id and Ship


# Statement:
# Write a program that takes in a letterclass ID of a ship and display the equivalent string class description of the given ID. Use the table below.

# Class ID	Ship Class
# B or b	    BattleShip
# C or c	    Cruiser
# D or d	    Destroyer
# F or f	    Frigate
# Input
# The first line contains an integer T, the total number of testcases. Then T lines follow, each line contains a character.

# Output
# For each test case, display the Ship Class depending on ID, in a new line.

# Constraints
# 1 ≤ T ≤ 1000
# Example
# Input

# 3 
# B
# c
# D

# Output
# BattleShip
# Cruiser
# Destroyer



# solutions:


# solution(1):
ship = {('b','B'): 'BattleShip', ('c','C'): 'Cruiser', ('d','D'): 'Destroyer', ('f','F'): 'Frigate'}
for _ in range(int(input())):
    n = input()
    print(next(v for k,v in ship.items() if n in k))

# solution(2):
ship = {'b':'BattleShip' , 'c': 'Cruiser','d': 'Destroyer', 'f': 'Frigate'}
for _ in range(int(input())):
    n = input().lower()
    print(ship[n])


# solution(3):
ship = {'b':'BattleShip' , 'c': 'Cruiser','d': 'Destroyer', 'f': 'Frigate'}
for _ in range(int(input())):
    print(ship[input().lower()])