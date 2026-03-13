"""
Advanced Calculator API Server
Flask-based REST API for the Advanced Calculator backend.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent directory to the path to import the calculator
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from advanced_calculator import AdvancedCalculator
except ImportError:
    print("Warning: Could not import AdvancedCalculator. Using mock implementation.")
    AdvancedCalculator = None

app = Flask(__name__)
CORS(app)  # Enable CORS for React frontend

# Global calculator instance
calculator = AdvancedCalculator() if AdvancedCalculator else None

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'Advanced Calculator API is running',
        'backend_available': calculator is not None
    })

@app.route('/api/calculate', methods=['POST'])
def calculate():
    """Perform a calculation."""
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No data provided'}), 400

        operation = data.get('operation')
        args = data.get('args', [])

        if not operation:
            return jsonify({'error': 'No operation specified'}), 400

        if not calculator:
            # Mock implementation for testing
            return mock_calculate(operation, args)

        # Use the real calculator
        result = calculator.calculate(operation, *args)

        return jsonify({
            'result': result,
            'operation': operation,
            'args': args
        })

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get calculation history."""
    if not calculator:
        return jsonify({'history': []})

    history = calculator.get_history()
    return jsonify({'history': history})

@app.route('/api/history', methods=['DELETE'])
def clear_history():
    """Clear calculation history."""
    if calculator:
        calculator.clear_history()
    return jsonify({'message': 'History cleared'})

def mock_calculate(operation, args):
    """Mock calculation for when backend is not available."""
    try:
        if operation == 'add':
            result = sum(args)
        elif operation == 'subtract' and len(args) == 2:
            result = args[0] - args[1]
        elif operation == 'multiply':
            result = 1
            for arg in args:
                result *= arg
        elif operation == 'divide' and len(args) == 2 and args[1] != 0:
            result = args[0] / args[1]
        elif operation == 'power' and len(args) == 2:
            result = args[0] ** args[1]
        elif operation == 'sqrt' and len(args) == 1:
            import math
            result = math.sqrt(args[0])
        elif operation == 'factorial' and len(args) == 1:
            import math
            result = math.factorial(int(args[0]))
        elif operation == 'log' and len(args) == 1:
            import math
            result = math.log10(args[0])
        elif operation == 'absolute' and len(args) == 1:
            result = abs(args[0])
        # Scientific functions
        elif operation == 'sin' and len(args) >= 1:
            import math
            angle = args[0]
            if len(args) > 1 and args[1]:  # degrees flag
                angle = math.radians(angle)
            result = math.sin(angle)
        elif operation == 'cos' and len(args) >= 1:
            import math
            angle = args[0]
            if len(args) > 1 and args[1]:  # degrees flag
                angle = math.radians(angle)
            result = math.cos(angle)
        elif operation == 'tan' and len(args) >= 1:
            import math
            angle = args[0]
            if len(args) > 1 and args[1]:  # degrees flag
                angle = math.radians(angle)
            result = math.tan(angle)
        elif operation == 'asin' and len(args) >= 1:
            import math
            value = args[0]
            if not -1 <= value <= 1:
                raise ValueError("Arcsine input must be between -1 and 1")
            result = math.asin(value)
            if len(args) > 1 and args[1]:  # degrees flag
                result = math.degrees(result)
        elif operation == 'acos' and len(args) >= 1:
            import math
            value = args[0]
            if not -1 <= value <= 1:
                raise ValueError("Arccosine input must be between -1 and 1")
            result = math.acos(value)
            if len(args) > 1 and args[1]:  # degrees flag
                result = math.degrees(result)
        elif operation == 'atan' and len(args) >= 1:
            import math
            value = args[0]
            result = math.atan(value)
            if len(args) > 1 and args[1]:  # degrees flag
                result = math.degrees(result)
        elif operation == 'ln' and len(args) == 1:
            import math
            if args[0] <= 0:
                raise ValueError("Natural logarithm requires positive numbers")
            result = math.log(args[0])
        elif operation == 'exp' and len(args) == 1:
            import math
            result = math.exp(args[0])
        elif operation == 'pow10' and len(args) == 1:
            result = 10 ** args[0]
        elif operation == 'pi':
            import math
            result = math.pi
        elif operation == 'e':
            import math
            result = math.e
        elif operation == 'rad2deg' and len(args) == 1:
            import math
            result = math.degrees(args[0])
        elif operation == 'deg2rad' and len(args) == 1:
            import math
            result = math.radians(args[0])
        elif operation == 'sinh' and len(args) == 1:
            import math
            result = math.sinh(args[0])
        elif operation == 'cosh' and len(args) == 1:
            import math
            result = math.cosh(args[0])
        elif operation == 'tanh' and len(args) == 1:
            import math
            result = math.tanh(args[0])
        else:
            raise ValueError(f'Unsupported operation: {operation}')

        return jsonify({
            'result': result,
            'operation': operation,
            'args': args
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/operations', methods=['GET'])
def get_operations():
    """Get list of available operations."""
    operations = [
        'add', 'subtract', 'multiply', 'divide',
        'power', 'sqrt', 'factorial', 'log',
        'modulo', 'absolute', 'percentage',
        # Scientific functions
        'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
        'ln', 'exp', 'pow10', 'pi', 'e',
        'rad2deg', 'deg2rad', 'sinh', 'cosh', 'tanh'
    ]
    return jsonify({'operations': operations})

if __name__ == '__main__':
    print("Starting Advanced Calculator API Server...")
    print("Available endpoints:")
    print("  GET  /api/health      - Health check")
    print("  POST /api/calculate   - Perform calculation")
    print("  GET  /api/history     - Get calculation history")
    print("  DELETE /api/history   - Clear history")
    print("  GET  /api/operations  - List available operations")
    print("\nServer will run on http://localhost:5000")

    app.run(debug=True, host='0.0.0.0', port=5000)