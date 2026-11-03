# Pattern 1: Import the whole module
import random
import os

number = random.randint(1, 10)
choice = random.choice(['apple', 'banana', 'cherry'])
print(number)
print(choice)
print(os.getcwd())