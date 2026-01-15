# Calc
num1 = float(input("#1: "))
num2 = float(input("#2: "))
num3 = float(input("#3: "))

def calculate_average(num1, num2, num3):
  return (num1 + num2 + num3)/3 

print(calculate_average(num1, num2, num3))

# Tax

num4 = float(input("Money: "))

def bill_total(num4):
    return (num4 * 0.1) + num4

print(bill_total(num4))

# Greet

hello = input("What is your name? ")

def name(hello):
    return hello

print(hello, ", hello.")
