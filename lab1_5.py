# Multiples of 3 & 5 ---

number = float(input("What number? "))

def check_multiple(number):
    if number % 3 == 0:
        if number % 5 == 0:
            return True
        else:
            return False
    else: return False

print(check_multiple(number))

# Password ---

input_string = input("What is the password? ")
input_password = "Python123"

def check_password(input_string):
  if input_string == input_password:
    return "access granted"
  else:
    return "access denied"

print(check_password(input_string))

# Taxable income ---
salary = float(input("What is your salary? "))

def calculate_federal_tax(salary):
  if salary < 11000.00:
    return salary * 0.1
  elif salary >= 11000.00 and salary < 44725.00:
    return salary * 0.12
  elif salary >= 44725.00 and salary < 95375.00:
    return salary * 0.22
  else:
    return salary * 0.24

print(calculate_federal_tax(salary))
