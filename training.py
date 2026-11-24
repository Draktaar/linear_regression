import sys

DATA_FILENAME = "data.csv"
RESULT_FILENAME = "thetas.txt"

def mse(theta0, theta1, data):
    

with open(DATA_FILENAME, 'r') as file:
    lines = file.readlines()[1:]
    data = 

try:
    open(RESULT_FILENAME, 'r').close()
except FileNotFoundError:
    open(RESULT_FILENAME, 'w').close()

with open(RESULT_FILENAME, 'w') as file:
    file.write("432,2535\n")

