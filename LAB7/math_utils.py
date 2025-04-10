# math_utils.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    # All functions are working
    print(mod(10, 3))
    print(add(5, 3))
    print(subtract(5, 3))
    print(multiply(5, 3))
    print(divide(5, 0))
    print(power(2, 3))





