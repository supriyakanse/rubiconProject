import math
import numpy as np
import requests

def simple_calculator():
  """
  Performs simple arithmetic operations.
  """
  operation = input("Select an operation: +, -, *, /")
  number_1 = float(input("Enter the first number: "))
  number_2 = float(input("Enter the second number: "))

  if operation == "+":
    print(number_1 + number_2)
  elif operation == "-":
    print(number_1 - number_2)
  elif operation == "*":
    print(number_1 * number_2)
  elif operation == "/":
    print(number_1 / number_2)
  else:
    print("Invalid operation")

def scientific_calculator():
  """
  Performs scientific calculations.
  """
  operation = input("Select an operation: ^, sqrt, log, sin, cos, tan")
  number = float(input("Enter the number: "))

  if operation == "^":
    print(math.pow(number, 2))
  elif operation == "sqrt":
    print(math.sqrt(number))
  elif operation == "log":
    print(math.log10(number))
  elif operation == "sin":
    print(math.sin(number))
  elif operation == "cos":
    print(math.cos(number))
  elif operation == "tan":
    print(math.tan(number))
  else:
    print("Invalid operation")

def fraction_calculator():
  """
  Performs calculations with fractions.
  """
  fraction_1 = input("Enter the first fraction: ")
  fraction_2 = input("Enter the second fraction: ")

  print(fraction_1 + fraction_2)
  print(fraction_1 - fraction_2)
  print(fraction_1 * fraction_2)
  print(fraction_1 / fraction_2)

def matrix_calculator():
  """
  Performs calculations with matrices.
  """
  print("Welcome to the matrix calculator!")
  print("What kind of calculation would you like to perform?")
  print("1. Matrix addition")
  print("2. Matrix subtraction")
  print("3. Matrix multiplication")
  print("4. Matrix transpose")
  print("5. Matrix determinant")
  print("6. Matrix inverse")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    matrix_addition()
  elif choice == 2:
    matrix_subtraction()
  elif choice == 3:
    matrix_multiplication()
  elif choice == 4:
    matrix_transpose()
  elif choice == 5:
    matrix_determinant()
  elif choice == 6:
    matrix_inverse()
  else:
    print("Invalid choice")

def matrix_addition():
  """
  Performs matrix addition.
  """
  matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
  matrix_2 = np.array([[7, 8, 9], [10, 11, 12]])

  print("Matrix 1:")
  print(matrix_1)

  print("Matrix 2:")
  print(matrix_2)

  print("Matrix addition:")
  print(matrix_1 + matrix_2)

def matrix_subtraction():
  """
  Performs matrix subtraction.
  """
  matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
  matrix_2 = np.array([[7, 8, 9], [10, 11, 12]])

  print("Matrix 1:")
  print(matrix_1)

  print("Matrix 2:")
  print(matrix_2)

  print("Matrix subtraction:")
  print(matrix_1 - matrix_2)

def matrix_multiplication():
  """
  Performs matrix multiplication.
  """
  matrix_1 = np.array([[1, 2, 3], [4, 5, 6]])
  matrix_2 = np.array([[7, 8], [9, 10], [11, 12]])

  print("Matrix 1:")
  print(matrix_1)

  print("Matrix 2:")
  print(matrix_2)

  print("Matrix multiplication:")
  print(matrix_1 @ matrix_2)

def matrix_transpose():
  """
  Performs matrix transpose.
  """
  matrix = np.array([[1, 2, 3], [4, 5, 6]])

  print("Matrix:")
  print(matrix)

  print("Matrix transpose:")
  print(matrix.transpose())

def matrix_determinant():
  """
  Calculates the determinant of a matrix.
  """
  matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  print("Matrix:")
  print(matrix)

  print("Determinant:")
  print(np.linalg.det(matrix))

def matrix_inverse():
  """
  Calculates the inverse of a matrix.
  """
  matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

  print("Matrix:")
  print(matrix)

  print("Inverse:")
  print(np.linalg.inv(matrix))


def unit_converter():
  
  
  """
  Converts units from one system to another.
  """
  print("Welcome to the unit converter!")
  print("What kind of unit conversion would you like to perform?")
  print("1. Length")
  print("2. Mass")
  print("3. Time")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    unit_converter_length()
  elif choice == 2:
    unit_converter_mass()
  elif choice == 3:
    unit_converter_time()
  else:
    print("Invalid choice")

def unit_converter_length():
  """
  Converts units of length.
  """
  print("What kind of length conversion would you like to perform?")
  print("1. Meters to centimeters")
  print("2. Meters to kilometers")
  print("3. Meters to feet")
  print("4. Meters to inches")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    print(100 * input("Enter the value in meters: "))
  elif choice == 2:
    print(1000 * input("Enter the value in meters: "))
  elif choice == 3:
    print(3.28084 * input("Enter the value in meters: "))
  elif choice == 4:
    print(39.3701 * input("Enter the value in meters: "))

def unit_converter_mass():
  """
  Converts units of mass.
  """
  print("What kind of mass conversion would you like to perform?")
  print("1. Kilograms to grams")
  print("2. Kilograms to pounds")
  print("3. Kilograms to ounces")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    print(1000 * input("Enter the value in kilograms: "))
  elif choice == 2:
    print(2.20462 * input("Enter the value in kilograms: "))
  elif choice == 3:
    print(35.274 * input("Enter the value in kilograms: "))

def unit_converter_time():
  """
  Converts units of time.
  """
  print("What kind of time conversion would you like to perform?")
  print("1. Seconds to milliseconds")
  print("2. Seconds to minutes")
  print("3. Seconds to hours")
  print("4. Days to seconds")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    print(1000 * input("Enter the value in seconds: "))
  elif choice == 2:
    print(60 * input("Enter the value in seconds: "))
  elif choice == 3:
    print(3600 * input("Enter the value in seconds: "))
  elif choice == 4:
    print(86400 * input("Enter the value in seconds: "))



def currency_converter():
  """
  Converts currencies from one currency to another.
  """
  print("Welcome to the currency converter!")
  print("What currencies would you like to convert?")
  print("1. USD to INR")
  print("2. INR to USD")
  print("3. EUR to USD")
  print("4. USD to EUR")
  print("5. GBP to USD")
  print("6. USD to GBP")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    source_currency = "USD"
    target_currency = "INR"
  elif choice == 2:
    source_currency = "INR"
    target_currency = "USD"
  elif choice == 3:
    source_currency = "EUR"
    target_currency = "USD"
  elif choice == 4:
    source_currency = "USD"
    target_currency = "EUR"
  elif choice == 5:
    source_currency = "GBP"
    target_currency = "USD"
  elif choice == 6:
    source_currency = "USD"
    target_currency = "GBP"
  else:
    print("Invalid choice")

  amount = float(input("Enter the amount: "))

  api_url = "https://api.exchangerate-api.com/v4/latest/{source_currency}".format(source_currency=source_currency)
  response = requests.get(api_url)

  if response.status_code == 200:
    data = response.json()
    exchange_rate = data["rates"][target_currency]
    print("The converted amount is {amount} {target_currency}.".format(amount=amount, target_currency=target_currency, exchange_rate=exchange_rate))
  else:
    print("An error occurred.")


def main():
  """
  The main function that controls the flow of the program.
  """
  print("Welcome to the calculator system!")
  print("What kind of calculation would you like to perform?")
  print("1. Simple calculator")
  print("2. Scientific calculator")
  print("3. Fraction calculator")
  print("4. Matrix calculator")
  print("5. Unit converter")
  print("6. Currency converter")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    simple_calculator()
  elif choice == 2:
    scientific_calculator()
  elif choice == 3:
    fraction_calculator()
  elif choice == 4:
    matrix_calculator()
  elif choice == 5:
    unit_converter()
  elif choice == 6:
    currency_converter()
  else:
    print("Invalid choice")

if __name__ == "__main__":
  main()
