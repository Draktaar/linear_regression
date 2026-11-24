import sys

mileage = input("Enter mileage: ")

try:
    mileage = float(mileage)
except ValueError:
    print("Please enter a valid number")
    sys.exit(1)

if mileage < 0:
    print("Mileage can't be negative")
    sys.exit(1)

try:
    with open('thetas.txt', 'r') as file:
        str0, str1 = file.readline().strip().split(',')
        theta0, theta1 = float(str0), float(str1)
except FileNotFoundError:
    theta0, theta1 = 0.0, 0.0

# TODO: convertir les thetas ou non ?

print(theta0 + (theta1 * mileage))