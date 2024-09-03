# math_operators_lesson

"""
Introduction to Python Mathematical Operators

Welcome to this lesson on Python mathematical operators! In this chapter, we'll explore 
the fundamental mathematical operations you can perform in Python. These operators are 
essential for any kind of numerical computation, from simple arithmetic to complex 
calculations.

We'll cover the following operators:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Modulus (%)
6. Exponentiation (**)
7. Floor Division (//)

Each operator will be explained with examples. Feel free to modify the numbers in the 
examples to see how the results change!
"""

def addition(a, b):
    """
    Addition Operator (+)
    Used to add two numbers together.
    
    Example: 5 + 3 = 8
    
    Try different numbers to see how it works!
    """
    return #a + b

def subtraction(a, b):
    """
    Subtraction Operator (-)
    Used to subtract the second number from the first.
    
    Example: 10 - 4 = 6
    
    Remember, the order matters in subtraction!
    """
    return #a - b

def multiplication(a, b):
    """
    Multiplication Operator (*)
    Used to multiply two numbers.
    
    Example: 6 * 7 = 42
    
    Multiplying by 0 always gives 0, and by 1 leaves the number unchanged.
    """
    return #a * b

def division(a, b):
    """
    Division Operator (/)
    Used to divide the first number by the second.
    
    Example: 15 / 3 = 5.0
    
    Note: In Python 3, division always returns a float.
    Be careful: division by zero is not allowed and will raise an error.
    """
    #if b == 0:
        #return "Error: Division by zero"
    return #a / b

def modulus(a, b):
    """
    Modulus Operator (%)
    Returns the remainder when the first number is divided by the second.
    
    Example: 17 % 5 = 2
    
    This is useful for checking divisibility or working with circular patterns.
    """
    #if b == 0:
        #return "Error: Modulus by zero"
    return #a % b

def exponentiation(a, b):
    """
    Exponentiation Operator (**)
    Raises the first number to the power of the second number.
    
    Example: 2 ** 3 = 8
    
    This is a quick way to calculate powers. Remember, any number to the power of 0 is 1.
    """
    return #a ** b

def floor_division(a, b):
    """
    Floor Division Operator (//)
    Divides the first number by the second and rounds down to the nearest integer.
    
    Example: 17 // 5 = 3
    
    This is useful when you need a whole number result from division.
    """
    #if b == 0:
        #return "Error: Division by zero"
    return #a // b

# Example usage
if __name__ == "__main__":
    print("Let's practice using these operators!")
    print("Addition: 5 + 3 =", addition(5, 3))
    print("Subtraction: 10 - 4 =", subtraction(10, 4))
    print("Multiplication: 6 * 7 =", multiplication(6, 7))
    print("Division: 15 / 3 =", division(15, 3))
    print("Modulus: 17 % 5 =", modulus(17, 5))
    print("Exponentiation: 2 ** 3 =", exponentiation(2, 3))
    print("Floor Division: 17 // 5 =", floor_division(17, 5))

    print("\nNow it's your turn! Try modifying the numbers in these examples.")
    print("You can also write your own expressions using these operators.")
    print("Remember to test edge cases, like dividing by zero or using negative numbers.")