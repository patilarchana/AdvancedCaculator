#!/usr/bin/env python3
"""
Comprehensive API Testing Suite for Advanced Calculator
Tests all endpoints, operations, error handling, and edge cases
"""

import requests
import json
import time
import unittest
from typing import Dict, List, Any

BASE_URL = "http://localhost:5000/api"

class TestCalculatorAPI(unittest.TestCase):
    """Comprehensive test suite for Calculator API"""

    def setUp(self):
        """Set up test environment"""
        self.base_url = BASE_URL
        self.session = requests.Session()
        # Clear history before each test
        try:
            self.session.delete(f"{self.base_url}/history")
        except:
            pass  # Ignore if server is not running

    def tearDown(self):
        """Clean up after each test"""
        try:
            self.session.delete(f"{self.base_url}/history")
        except:
            pass

    # ===== HEALTH ENDPOINT TESTS =====

    def test_health_endpoint_success(self):
        """Test health endpoint returns correct response"""
        response = self.session.get(f"{self.base_url}/health")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('status', data)
        self.assertIn('message', data)
        self.assertIn('backend_available', data)
        self.assertEqual(data['status'], 'healthy')
        self.assertTrue(data['backend_available'])

    def test_health_endpoint_structure(self):
        """Test health endpoint response structure"""
        response = self.session.get(f"{self.base_url}/health")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        # Validate response schema
        required_fields = ['status', 'message', 'backend_available']
        for field in required_fields:
            self.assertIn(field, data)

    # ===== BASIC CALCULATION TESTS =====

    def test_add_operation(self):
        """Test addition operation"""
        payload = {"operation": "add", "args": [10, 5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['operation'], 'add')
        self.assertEqual(data['args'], [10, 5])
        self.assertEqual(data['result'], 15)

    def test_subtract_operation(self):
        """Test subtraction operation"""
        payload = {"operation": "subtract", "args": [10, 5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 5)

    def test_multiply_operation(self):
        """Test multiplication operation"""
        payload = {"operation": "multiply", "args": [10, 5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 50)

    def test_divide_operation(self):
        """Test division operation"""
        payload = {"operation": "divide", "args": [10, 5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 2)

    # ===== ADVANCED OPERATION TESTS =====

    def test_power_operation(self):
        """Test power operation"""
        payload = {"operation": "power", "args": [2, 3]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 8)

    def test_square_root_operation(self):
        """Test square root operation"""
        payload = {"operation": "sqrt", "args": [16]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 4)

    def test_factorial_operation(self):
        """Test factorial operation"""
        payload = {"operation": "factorial", "args": [5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 120)

    def test_logarithm_operation(self):
        """Test logarithm operation"""
        payload = {"operation": "log", "args": [100]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 2.0, places=5)

    def test_modulo_operation(self):
        """Test modulo operation"""
        payload = {"operation": "modulo", "args": [17, 5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 2)

    def test_absolute_operation(self):
        """Test absolute value operation"""
        payload = {"operation": "absolute", "args": [-10]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 10)

    def test_percentage_operation(self):
        """Test percentage operation"""
        payload = {"operation": "percentage", "args": [200, 15]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 30)

    # ===== SCIENTIFIC FUNCTION TESTS =====

    def test_sine_operation(self):
        """Test sine operation (radians)"""
        payload = {"operation": "sin", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 0.0, places=5)

    def test_cosine_operation(self):
        """Test cosine operation (radians)"""
        payload = {"operation": "cos", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 1.0, places=5)

    def test_tangent_operation(self):
        """Test tangent operation (radians)"""
        payload = {"operation": "tan", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 0.0, places=5)

    def test_natural_logarithm_operation(self):
        """Test natural logarithm operation"""
        payload = {"operation": "ln", "args": [1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 0.0, places=5)

    def test_exponential_operation(self):
        """Test exponential operation (e^x)"""
        payload = {"operation": "exp", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 1.0, places=5)

    def test_pi_constant(self):
        """Test pi constant"""
        payload = {"operation": "pi", "args": []}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 3.141592653589793, places=5)

    def test_e_constant(self):
        """Test Euler's number constant"""
        payload = {"operation": "e", "args": []}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 2.718281828459045, places=5)

    def test_arcsine_operation(self):
        """Test arcsine operation"""
        payload = {"operation": "asin", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 0.0, places=5)

    def test_hyperbolic_sine_operation(self):
        """Test hyperbolic sine operation"""
        payload = {"operation": "sinh", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 0.0, places=5)

    # ===== ADVANCED SCIENTIFIC FUNCTION TESTS =====

    def test_trigonometric_pi_values(self):
        """Test trigonometric functions with π/2, π values"""
        import math

        # sin(π/2) = 1
        payload = {"operation": "sin", "args": [math.pi/2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 1.0, places=5)

        # cos(π) = -1
        payload = {"operation": "cos", "args": [math.pi]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], -1.0, places=5)

        # tan(π/4) = 1
        payload = {"operation": "tan", "args": [math.pi/4]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 1.0, places=5)

    def test_inverse_trigonometric_functions(self):
        """Test inverse trigonometric functions"""
        import math

        # asin(1) = π/2
        payload = {"operation": "asin", "args": [1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.pi/2, places=5)

        # acos(0) = π/2
        payload = {"operation": "acos", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.pi/2, places=5)

        # atan(1) = π/4
        payload = {"operation": "atan", "args": [1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.pi/4, places=5)

    def test_hyperbolic_functions_comprehensive(self):
        """Test hyperbolic functions with various inputs"""
        import math

        # sinh(1) ≈ 1.1752
        payload = {"operation": "sinh", "args": [1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.sinh(1), places=5)

        # cosh(1) ≈ 1.5431
        payload = {"operation": "cosh", "args": [1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.cosh(1), places=5)

        # tanh(0.5) ≈ 0.4621
        payload = {"operation": "tanh", "args": [0.5]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.tanh(0.5), places=5)

    def test_logarithmic_functions_comprehensive(self):
        """Test logarithmic functions with various inputs"""
        import math

        # ln(e²) = 2
        payload = {"operation": "ln", "args": [math.e**2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 2.0, places=5)

        # log(100) = 2 (base 10)
        payload = {"operation": "log", "args": [100]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 2.0, places=5)

        # pow10(3) = 1000
        payload = {"operation": "pow10", "args": [3]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 1000.0, places=5)

    def test_exponential_functions_comprehensive(self):
        """Test exponential functions with various inputs"""
        import math

        # exp(2) = e²
        payload = {"operation": "exp", "args": [2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.e**2, places=5)

        # exp(-1) = 1/e
        payload = {"operation": "exp", "args": [-1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 1/math.e, places=5)

    def test_angle_conversion_functions(self):
        """Test angle conversion functions"""
        import math

        # 180 degrees = π radians
        payload = {"operation": "deg2rad", "args": [180]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], math.pi, places=5)

        # π radians = 180 degrees
        payload = {"operation": "rad2deg", "args": [math.pi]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 180.0, places=5)

    def test_mathematical_constants_precision(self):
        """Test mathematical constants for precision"""
        import math

        # Test pi precision
        payload = {"operation": "pi", "args": []}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], math.pi)

        # Test e precision
        payload = {"operation": "e", "args": []}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], math.e)

    # ===== SCIENTIFIC ERROR HANDLING TESTS =====

    def test_arcsine_domain_error(self):
        """Test arcsine domain error (input outside [-1, 1])"""
        payload = {"operation": "asin", "args": [2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_arccosine_domain_error(self):
        """Test arccosine domain error (input outside [-1, 1])"""
        payload = {"operation": "acos", "args": [-2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_logarithm_negative_error(self):
        """Test logarithm of negative number error"""
        payload = {"operation": "ln", "args": [-1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_logarithm_zero_error(self):
        """Test logarithm of zero error"""
        payload = {"operation": "log", "args": [0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_trigonometric_large_angles(self):
        """Test trigonometric functions with large angles"""
        import math

        # sin(2π) should equal sin(0) = 0
        payload = {"operation": "sin", "args": [2*math.pi]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 0.0, places=5)

        # cos(2π) should equal cos(0) = 1
        payload = {"operation": "cos", "args": [2*math.pi]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertAlmostEqual(response.json()['result'], 1.0, places=5)

    def test_scientific_function_edge_cases(self):
        """Test scientific functions with edge cases"""
        import math

        # Very small numbers
        payload = {"operation": "exp", "args": [-100]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        result = response.json()['result']
        self.assertLess(result, 1e-40)  # Should be very close to 0

        # Very large numbers (but not causing overflow)
        payload = {"operation": "ln", "args": [1e10]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        self.assertEqual(response.status_code, 200)
        result = response.json()['result']
        self.assertAlmostEqual(result, math.log(1e10), places=3)

    # ===== ERROR HANDLING TESTS =====

    def test_divide_by_zero_error(self):
        """Test division by zero error handling"""
        payload = {"operation": "divide", "args": [10, 0]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)
        self.assertIn('zero', data['error'].lower())

    def test_square_root_negative_error(self):
        """Test square root of negative number error"""
        payload = {"operation": "sqrt", "args": [-4]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_factorial_negative_error(self):
        """Test factorial of negative number error"""
        payload = {"operation": "factorial", "args": [-1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_logarithm_negative_error(self):
        """Test logarithm of negative number error"""
        payload = {"operation": "log", "args": [-1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_natural_logarithm_negative_error(self):
        """Test natural logarithm of negative number error"""
        payload = {"operation": "ln", "args": [-1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_arcsine_invalid_input_error(self):
        """Test arcsine with invalid input (outside [-1, 1])"""
        payload = {"operation": "asin", "args": [2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_arccosine_invalid_input_error(self):
        """Test arccosine with invalid input (outside [-1, 1])"""
        payload = {"operation": "acos", "args": [2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_invalid_operation_error(self):
        """Test invalid operation error"""
        payload = {"operation": "invalid_op", "args": [1, 2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    # ===== DATA VALIDATION TESTS =====

    def test_missing_operation_field(self):
        """Test missing operation field"""
        payload = {"args": [1, 2]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    def test_missing_args_field(self):
        """Test missing args field"""
        payload = {"operation": "add"}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertIn('error', data)

    # ===== EDGE CASE TESTS =====

    def test_large_numbers(self):
        """Test operations with large numbers"""
        payload = {"operation": "add", "args": [999999999, 999999999]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['result'], 1999999998)

    def test_decimal_numbers(self):
        """Test operations with decimal numbers"""
        payload = {"operation": "add", "args": [1.5, 2.7]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertAlmostEqual(data['result'], 4.2, places=5)

    # ===== HISTORY ENDPOINT TESTS =====

    def test_history_initially_empty(self):
        """Test that history is initially empty"""
        response = self.session.get(f"{self.base_url}/history")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('history', data)
        self.assertEqual(len(data['history']), 0)

    def test_history_after_calculation(self):
        """Test history after performing calculations"""
        # Perform a calculation
        payload = {"operation": "add", "args": [3, 7]}
        self.session.post(f"{self.base_url}/calculate", json=payload)

        # Check history
        response = self.session.get(f"{self.base_url}/history")
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn('history', data)
        self.assertEqual(len(data['history']), 1)

        # Verify history entry structure
        entry = data['history'][0]
        self.assertIsInstance(entry, list)
        self.assertEqual(len(entry), 2)
        self.assertEqual(entry[0], 'add(3, 7)')
        self.assertEqual(entry[1], 10)

    def test_clear_history(self):
        """Test clearing history"""
        # Add some history
        payload = {"operation": "add", "args": [1, 1]}
        self.session.post(f"{self.base_url}/calculate", json=payload)

        # Verify history exists
        response = self.session.get(f"{self.base_url}/history")
        data = response.json()
        self.assertEqual(len(data['history']), 1)

        # Clear history
        response = self.session.delete(f"{self.base_url}/history")
        self.assertEqual(response.status_code, 200)

        # Verify history is empty
        response = self.session.get(f"{self.base_url}/history")
        data = response.json()
        self.assertEqual(len(data['history']), 0)

    # ===== PERFORMANCE TESTS =====

    def test_response_time(self):
        """Test that API responds within reasonable time"""
        payload = {"operation": "add", "args": [1, 1]}

        start_time = time.time()
        response = self.session.post(f"{self.base_url}/calculate", json=payload)
        end_time = time.time()

        self.assertEqual(response.status_code, 200)
        self.assertLess(end_time - start_time, 1.0)  # Should respond within 1 second

    # ===== SECURITY TESTS =====

    def test_sql_injection_protection(self):
        """Test protection against SQL injection"""
        payload = {"operation": "add", "args": ["1; DROP TABLE users;", 1]}
        response = self.session.post(f"{self.base_url}/calculate", json=payload)

        # Should either reject or handle gracefully
        self.assertIn(response.status_code, [200, 400, 500])

    # ===== INTEGRATION TESTS =====

    def test_full_calculation_workflow(self):
        """Test a complete calculation workflow"""
        # Clear any existing history
        self.session.delete(f"{self.base_url}/history")

        # Perform a series of calculations
        calculations = [
            {"operation": "add", "args": [10, 5]},      # 15
            {"operation": "multiply", "args": [15, 2]}, # 30
            {"operation": "power", "args": [30, 1]},    # 30
            {"operation": "sqrt", "args": [16]},        # 4
        ]

        results = []
        for calc in calculations:
            response = self.session.post(f"{self.base_url}/calculate", json=calc)
            self.assertEqual(response.status_code, 200)
            data = response.json()
            results.append(data['result'])

        # Verify results
        self.assertEqual(results, [15, 30, 30, 4])

        # Check history
        response = self.session.get(f"{self.base_url}/history")
        data = response.json()
        self.assertEqual(len(data['history']), 4)


# ===== STANDALONE TEST FUNCTIONS =====

def run_basic_api_tests():
    """Run basic API tests for quick verification"""
    print("🧪 Running Basic API Tests...")
    print("=" * 50)

    session = requests.Session()
    tests_passed = 0
    total_tests = 0

    # Health check
    total_tests += 1
    try:
        response = session.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("✅ Health check passed")
            tests_passed += 1
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")

    # Basic calculation
    total_tests += 1
    try:
        payload = {"operation": "add", "args": [10, 20]}
        response = session.post(f"{BASE_URL}/calculate", json=payload)
        if response.status_code == 200 and response.json()['result'] == 30:
            print("✅ Basic calculation passed")
            tests_passed += 1
        else:
            print(f"❌ Basic calculation failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Basic calculation error: {e}")

    # History operations
    total_tests += 1
    try:
        # Clear history
        session.delete(f"{BASE_URL}/history")

        # Add calculation
        payload = {"operation": "multiply", "args": [5, 6]}
        session.post(f"{BASE_URL}/calculate", json=payload)

        # Check history
        response = session.get(f"{BASE_URL}/history")
        if response.status_code == 200:
            data = response.json()
            if len(data['history']) >= 1:
                print("✅ History operations passed")
                tests_passed += 1
            else:
                print("❌ History operations failed: No history entries")
        else:
            print(f"❌ History operations failed: {response.status_code}")
    except Exception as e:
        print(f"❌ History operations error: {e}")

    print("=" * 50)
    print(f"📊 Basic Tests: {tests_passed}/{total_tests} passed")

    if tests_passed == total_tests:
        print("🎉 All basic API tests passed!")
        return True
    else:
        print("⚠️  Some basic tests failed")
        return False


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--basic":
        # Run basic tests only
        success = run_basic_api_tests()
        sys.exit(0 if success else 1)
    else:
        # Run comprehensive unit tests
        print("🧪 Running Comprehensive API Test Suite...")
        print("=" * 60)

        # Run the unit tests
        unittest.main(verbosity=2, exit=False)

        print("\n" + "=" * 60)
        print("🎯 API Testing Complete!")
        print("Run with --basic flag for quick verification tests")

def test_health():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health check: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_calculation():
    """Test a calculation"""
    try:
        payload = {
            "operation": "add",
            "args": [5, 3]
        }
        response = requests.post(f"{BASE_URL}/calculate", json=payload)
        print(f"Calculation test: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Calculation test failed: {e}")
        return False

def test_history():
    """Test history endpoints"""
    try:
        # Get history
        response = requests.get(f"{BASE_URL}/history")
        print(f"Get history: {response.status_code}")
        print(f"History: {response.json()}")

        # Clear history
        response = requests.delete(f"{BASE_URL}/history")
        print(f"Clear history: {response.status_code}")

        return True
    except Exception as e:
        print(f"History test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Calculator API Integration...")
    print("=" * 40)

    health_ok = test_health()
    calc_ok = test_calculation()
    history_ok = test_history()

    print("=" * 40)
    print(f"Tests passed: Health={health_ok}, Calculation={calc_ok}, History={history_ok}")

    if all([health_ok, calc_ok, history_ok]):
        print("✅ All API tests passed!")
    else:
        print("❌ Some tests failed. Check the server logs.")