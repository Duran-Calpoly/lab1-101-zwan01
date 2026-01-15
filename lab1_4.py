# Calc
num1 = float(input("#1: "))
num2 = float(input("#2: "))
num3 = float(input("#3: "))

def calculate_average(num1, num2, num3):
  return (num1 + num2 + num3)/3 

print(calculate_average(num1, num2, num3))

# Tax

bill_total = float(input("Money: "))

def add_tax(bill_total):
    return (bill_total * 0.1) + bill_total

print(add_tax(bill_total))

# Greet


def greet_user(name):
    return "Hello, " + name

name = input("What is your name? ")

print(greet_user(name))
