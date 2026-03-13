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
