"""
Advanced Calculator for Python Learning
A comprehensive calculator with advanced operations and features.
"""

import math
from typing import Union, List, Tuple


class AdvancedCalculator:
    """An advanced calculator with support for multiple operations and history."""
    
    def __init__(self):
        """Initialize the calculator with an empty history."""
        self.history: List[Tuple[str, Union[int, float]]] = []
    
    # ===== BASIC OPERATIONS =====
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return a + b
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide a by b with error handling."""
        if b == 0:
            raise ValueError("Error: Cannot divide by zero")
        return a / b
    
    # ===== ADVANCED OPERATIONS =====
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate base raised to the power of exponent."""
        return base ** exponent
    
    def modulo(self, a: int, b: int) -> int:
        """Return remainder of a divided by b."""
        if b == 0:
            raise ValueError("Error: Cannot divide by zero")
        return a % b
    
    def square_root(self, num: Union[int, float]) -> float:
        """Calculate the square root of a number."""
        if num < 0:
            raise ValueError("Error: Cannot calculate square root of negative number")
        return math.sqrt(num)
    
    def absolute_value(self, num: Union[int, float]) -> Union[int, float]:
        """Return the absolute value of a number."""
        return abs(num)
    
    def percentage(self, num: Union[int, float], percent: Union[int, float]) -> Union[int, float]:
        """Calculate a percentage of a number."""
        return (num * percent) / 100
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of n (n!)."""
        if n < 0:
            raise ValueError("Error: Cannot calculate factorial of negative number")
        if not isinstance(n, int):
            raise ValueError("Error: Factorial only works with integers")
        return math.factorial(n)
    
    def logarithm(self, num: Union[int, float], base: Union[int, float] = 10) -> float:
        """Calculate logarithm of a number with specified base (default is base 10)."""
        if num <= 0:
            raise ValueError("Error: Logarithm requires positive numbers")
        if base <= 0 or base == 1:
            raise ValueError("Error: Log base must be positive and not equal to 1")
        return math.log(num, base)
    
    # ===== SCIENTIFIC FUNCTIONS =====
    def sine(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate sine of an angle (in radians by default, or degrees if specified)."""
        if degrees:
            angle = math.radians(angle)
        return math.sin(angle)
    
    def cosine(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate cosine of an angle (in radians by default, or degrees if specified)."""
        if degrees:
            angle = math.radians(angle)
        return math.cos(angle)
    
    def tangent(self, angle: Union[int, float], degrees: bool = False) -> float:
        """Calculate tangent of an angle (in radians by default, or degrees if specified)."""
        if degrees:
            angle = math.radians(angle)
        return math.tan(angle)
    
    def arcsine(self, value: Union[int, float], degrees: bool = False) -> float:
        """Calculate arcsine (inverse sine) of a value."""
        if not -1 <= value <= 1:
            raise ValueError("Error: Arcsine input must be between -1 and 1")
        result = math.asin(value)
        return math.degrees(result) if degrees else result
    
    def arccosine(self, value: Union[int, float], degrees: bool = False) -> float:
        """Calculate arccosine (inverse cosine) of a value."""
        if not -1 <= value <= 1:
            raise ValueError("Error: Arccosine input must be between -1 and 1")
        result = math.acos(value)
        return math.degrees(result) if degrees else result
    
    def arctangent(self, value: Union[int, float], degrees: bool = False) -> float:
        """Calculate arctangent (inverse tangent) of a value."""
        result = math.atan(value)
        return math.degrees(result) if degrees else result
    
    def natural_logarithm(self, num: Union[int, float]) -> float:
        """Calculate natural logarithm (base e) of a number."""
        if num <= 0:
            raise ValueError("Error: Natural logarithm requires positive numbers")
        return math.log(num)
    
    def exponential(self, exponent: Union[int, float]) -> float:
        """Calculate e raised to the power of exponent (e^x)."""
        return math.exp(exponent)
    
    def power_of_ten(self, exponent: Union[int, float]) -> float:
        """Calculate 10 raised to the power of exponent (10^x)."""
        return 10 ** exponent
    
    def pi_constant(self) -> float:
        """Return the mathematical constant π (pi)."""
        return math.pi
    
    def e_constant(self) -> float:
        """Return the mathematical constant e (Euler's number)."""
        return math.e
    
    def radians_to_degrees(self, radians: Union[int, float]) -> float:
        """Convert radians to degrees."""
        return math.degrees(radians)
    
    def degrees_to_radians(self, degrees: Union[int, float]) -> float:
        """Convert degrees to radians."""
        return math.radians(degrees)
    
    def hyperbolic_sine(self, value: Union[int, float]) -> float:
        """Calculate hyperbolic sine of a value."""
        return math.sinh(value)
    
    def hyperbolic_cosine(self, value: Union[int, float]) -> float:
        """Calculate hyperbolic cosine of a value."""
        return math.cosh(value)
    
    def hyperbolic_tangent(self, value: Union[int, float]) -> float:
        """Calculate hyperbolic tangent of a value."""
        return math.tanh(value)
    
    def average(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate the average of a list of numbers."""
        if not numbers:
            raise ValueError("Error: Cannot calculate average of empty list")
        return sum(numbers) / len(numbers)
    
    # ===== HISTORY TRACKING =====
    def calculate(self, operation: str, *args) -> Union[int, float]:
        """
        Execute an operation and track it in history.
        
        Args:
            operation: The operation to perform
            *args: Arguments for the operation
        
        Returns:
            The result of the operation
        """
        operations = {
            'add': self.add,
            'subtract': self.subtract,
            'multiply': self.multiply,
            'divide': self.divide,
            'power': self.power,
            'modulo': self.modulo,
            'sqrt': self.square_root,
            'abs': self.absolute_value,
            'absolute': self.absolute_value,
            'percentage': self.percentage,
            'factorial': self.factorial,
            'log': self.logarithm,
            'average': self.average,
            # Scientific functions
            'sin': self.sine,
            'cos': self.cosine,
            'tan': self.tangent,
            'asin': self.arcsine,
            'acos': self.arccosine,
            'atan': self.arctangent,
            'ln': self.natural_logarithm,
            'exp': self.exponential,
            'pow10': self.power_of_ten,
            'pi': self.pi_constant,
            'e': self.e_constant,
            'rad2deg': self.radians_to_degrees,
            'deg2rad': self.degrees_to_radians,
            'sinh': self.hyperbolic_sine,
            'cosh': self.hyperbolic_cosine,
            'tanh': self.hyperbolic_tangent,
        }
        
        if operation not in operations:
            raise ValueError(f"Error: Unknown operation '{operation}'")
        
        try:
            result = operations[operation](*args)
            self.history.append((f"{operation}{args}", result))
            return result
        except Exception as e:
            raise e
    
    def get_history(self) -> List[Tuple[str, Union[int, float]]]:
        """Return the calculation history."""
        return self.history.copy()
    
    def clear_history(self):
        """Clear the calculation history."""
        self.history.clear()
    
    def print_history(self):
        """Print the calculation history in a readable format."""
        if not self.history:
            print("No history available")
            return
        
        print("\n===== CALCULATION HISTORY =====")
        for i, (operation, result) in enumerate(self.history, 1):
            print(f"{i}. {operation} = {result}")
        print("=" * 30)


# ===== INTERACTIVE MODE =====
def interactive_calculator():
    """Run the calculator in interactive mode."""
    calc = AdvancedCalculator()
    
    print("\n" + "=" * 40)
    print("     ADVANCED CALCULATOR")
    print("=" * 40)
    print("\nAvailable operations:")
    print("  add, subtract, multiply, divide")
    print("  power, modulo, sqrt, abs")
    print("  percentage, factorial, log, average")
    print("  history, clear_history, exit")
    print("=" * 40 + "\n")
    
    while True:
        try:
            user_input = input("Enter operation (or 'help' for options): ").strip().lower()
            
            if user_input == 'exit':
                print("Thank you for using Advanced Calculator!")
                break
            
            elif user_input == 'help':
                print("\nOperations Guide:")
                print("  add <a> <b>           : a + b")
                print("  subtract <a> <b>      : a - b")
                print("  multiply <a> <b>      : a × b")
                print("  divide <a> <b>        : a ÷ b")
                print("  power <base> <exp>    : base^exponent")
                print("  modulo <a> <b>        : a % b (remainder)")
                print("  sqrt <num>            : √num")
                print("  abs <num>             : |num|")
                print("  percentage <num> <%>  : calculate percentage")
                print("  factorial <n>         : n!")
                print("  log <num> [base]      : logarithm (default base 10)")
                print("  average <n1> <n2> ... : average of numbers")
                print("  history               : show calculation history")
                print("  clear_history         : clear history\n")
            
            elif user_input == 'history':
                calc.print_history()
            
            elif user_input == 'clear_history':
                calc.clear_history()
                print("History cleared!")
            
            else:
                parts = user_input.split()
                if not parts:
                    continue
                
                operation = parts[0]
                args = [float(x) if '.' in x else int(x) for x in parts[1:]]
                
                result = calc.calculate(operation, *args)
                print(f"Result: {result}\n")
        
        except ValueError as e:
            print(f"{e}\n")
        except Exception as e:
            print(f"Error: {e}\n")


# ===== EXAMPLE USAGE =====
if __name__ == "__main__":
    # Example: Using the calculator programmatically
    print("=== ADVANCED CALCULATOR EXAMPLES ===\n")
    
    calc = AdvancedCalculator()
    
    # Basic operations
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"10 - 5 = {calc.subtract(10, 5)}")
    print(f"10 × 5 = {calc.multiply(10, 5)}")
    print(f"10 ÷ 5 = {calc.divide(10, 5)}")
    
    # Advanced operations
    print(f"\n2^8 = {calc.power(2, 8)}")
    print(f"17 % 5 = {calc.modulo(17, 5)}")
    print(f"√16 = {calc.square_root(16)}")
    print(f"|−42| = {calc.absolute_value(-42)}")
    print(f"20% of 150 = {calc.percentage(150, 20)}")
    print(f"5! = {calc.factorial(5)}")
    print(f"log₁₀(100) = {calc.logarithm(100)}")
    print(f"Average of [5, 10, 15, 20] = {calc.average([5, 10, 15, 20])}")
    
    # Uncomment the line below to run interactive mode
    # interactive_calculator()
