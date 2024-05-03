# calculator.py (add-feature branch)

def add(a, b):
    return a + b

def main():
    print("Welcome to Simple Calculator!")
    print("Select operation:")
    print("1. Add")

    choice = '1'  # Fixed choice for addition

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))

if __name__ == "__main__":
    main()
