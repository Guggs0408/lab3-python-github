# A Python Calculator
def add(a, b):
    sum = a + b
    return sum

def subtract(a, b):
    difference = a - b
    return difference

def multiply(a, b):
    product = a * b
    return product

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
        return None
    quotient = a / b
    return quotient

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def percentage(a, b):
    if b == 0:
        print("Cannot calculate percentage with a denominator of zero.")
        return None
    percent = (a / b) * 100
    return percent


while True:

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Even or Odd")
    print("6. Percentage")
    print("7. Exit")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    if choice == '1':
        print(f"The sum is: {add(num1, num2)}")
    elif choice == '2':
        print(f"The difference is: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"The product is: {multiply(num1, num2)}")
    elif choice == '4':
        result = divide(num1, num2)
        if result is not None:
            print(f"The quotient is: {result}")
    elif choice == '5':
        print(f"{num1} is {even_odd(num1)}")
        print(f"{num2} is {even_odd(num2)}")
    elif choice == '6':
        result = percentage(num1, num2)
        if result is not None:
            print(f"{num1} is {result}% of {num2}")
    elif choice == '7':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input")
