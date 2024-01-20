# prompt: create a program that mini calculator

def add(num1, num2):
  return num1 + num2
def subtract(num1, num2):
  return num1 - num2
def multiply(num1, num2):
  return num1 * num2
def divide(num1, num2):
  return num1 / num2
def power(num1, num2):
  return num1 ** num2

def main():
  print("Welcome to the mini calculator!")
  while True:
    print("Enter two numbers and an operator (+, -, *, /, ^):")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator: ")
    result = 0
    if operator == "+":
      result = add(num1, num2)
    elif operator == "-":
      result = subtract(num1, num2)
    elif operator == "*":
      result = multiply(num1, num2)
    elif operator == "/":
      result = divide(num1, num2)
    elif operator == "^":
      result = power(num1, num2)
    else:
      print("Invalid operator!")
    print(f"The result is {result}")
    print("Do you want to continue? (y/n)")
    if input().lower() == "n":
      break
  print("Goodbye!")

if __name__ == "__main__":
  main()
