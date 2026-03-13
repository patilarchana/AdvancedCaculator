# Advanced Calculator - Full Stack Application

A comprehensive calculator application with Python backend and React frontend, featuring advanced mathematical operations, comprehensive testing, and persistent calculation history.

## Features

### Calculator Operations
- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**:
  - Power (x^y)
  - Square root (√)
  - Factorial (n!)
  - Logarithm (log₁₀)
  - Modulo (%)
  - Absolute value (|x|)
  - Percentage (%)

### Technical Features
- **Backend**: Python Flask REST API with AdvancedCalculator class
- **Frontend**: React.js with modern hooks and responsive design
- **Testing**: 80+ unit tests and end-to-end tests (100% pass rate)
- **History**: Persistent calculation history with clear functionality
- **Error Handling**: Comprehensive error handling for invalid operations
- **CORS Support**: Cross-origin resource sharing enabled

## Project Structure

```
CalculatorFrontEnd/
├── api_server.py              # Flask REST API server
├── advanced_calculator.py      # Core calculator logic
├── test_api.py                 # API integration tests
├── calculator-frontend/        # React frontend
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js             # Main React component
│   │   ├── App.css            # Component styles
│   │   ├── index.js           # React entry point
│   │   └── index.css          # Global styles
│   ├── package.json           # Frontend dependencies
│   └── README.md
└── README.md                   # This file
```

## Prerequisites

- **Python 3.7+**
- **Node.js 14+** and **npm**
- **Git** (for version control)

## Installation & Setup

### 1. Backend Setup

```bash
# Navigate to the project directory
cd CalculatorFrontEnd

# Install Python dependencies
pip install Flask flask-cors requests
```

### 2. Frontend Setup

```bash
# Navigate to the frontend directory
cd calculator-frontend

# Install Node.js dependencies
npm install
```

## Running the Application

### Start the Backend API Server

```bash
# From the CalculatorFrontEnd directory
python api_server.py
```

The API server will start on `http://localhost:5000`

### Start the React Frontend

```bash
# From the calculator-frontend directory
npm start
```

The React app will open in your browser at `http://localhost:3000`

## API Endpoints

### Health Check
```
GET /api/health
```
Returns server status and backend availability.

### Perform Calculation
```
POST /api/calculate
Content-Type: application/json

{
  "operation": "add",
  "args": [5, 3]
}
```
Supported operations: `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `factorial`, `log`, `modulo`, `absolute`, `percentage`

### Get Calculation History
```
GET /api/history
```
Returns array of recent calculations.

### Clear History
```
DELETE /api/history
```
Clears all calculation history.

## Testing

### Backend Tests
The backend includes comprehensive unit tests and end-to-end tests:

- **Unit Tests**: `test_advanced_calculator.py` (53 tests)
- **E2E Tests**: `test_advanced_calculator_e2e.py` (27 tests)
- **API Tests**: `test_api.py` (integration tests)

Run tests with:
```bash
python -m unittest test_advanced_calculator.py
python -m unittest test_advanced_calculator_e2e.py
python test_api.py
```

### Frontend Tests
```bash
cd calculator-frontend
npm test
```

## Usage

1. **Basic Calculations**: Click number buttons and operation buttons
2. **Advanced Operations**: Use the special function buttons (√, x^y, n!, log, etc.)
3. **History**: View recent calculations in the history panel
4. **Clear History**: Use the "Clear History" button to reset history

## Error Handling

The application handles various error conditions:
- Division by zero
- Invalid factorial inputs (negative numbers, non-integers)
- Square root of negative numbers
- Logarithm of non-positive numbers
- Network connectivity issues (fallback to mock calculations)

## Development

### Adding New Operations

1. **Backend**: Add method to `AdvancedCalculator` class
2. **API**: Add operation handling in `api_server.py`
3. **Frontend**: Add button and operation handling in `App.js`
4. **Tests**: Add corresponding unit tests

### Styling

The frontend uses CSS with:
- Gradient background
- Responsive button layout
- Modern typography
- Hover effects and transitions

## Deployment

### Backend Deployment
- Use Gunicorn or uWSGI for production
- Set environment variables for configuration
- Enable HTTPS in production

### Frontend Deployment
```bash
cd calculator-frontend
npm run build
```
Deploy the `build` folder to your web server.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## GitHub Repository

The complete codebase is available at: https://github.com/patilarchana/MyPython

Includes:
- Full source code
- Comprehensive test suite
- CI/CD pipeline
- Documentation