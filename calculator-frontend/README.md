# Advanced Calculator Frontend

A modern React-based frontend for the Advanced Calculator, providing an intuitive user interface for mathematical operations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power, square root, factorial, logarithm, modulo, absolute value, percentage
- **Real-time Calculation**: Instant results with proper error handling
- **Calculation History**: Track your recent calculations
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean, intuitive interface with smooth animations

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Navigate to the calculator-frontend directory:
   ```bash
   cd calculator-frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### Backend Integration

This frontend is designed to work with the Python Advanced Calculator backend. To enable full functionality:

1. Start the Python backend server (see backend README)
2. Update the API endpoints in `src/App.js` to point to your backend URL

## Usage

### Basic Calculations
- Click number buttons to input digits
- Use operator buttons (+, -, ×, ÷) for basic operations
- Press "=" to calculate the result
- Press "C" to clear the display

### Advanced Operations
- **√**: Calculate square root
- **x^y**: Calculate power (x raised to y)
- **n!**: Calculate factorial
- **log**: Calculate base-10 logarithm
- **%**: Calculate percentage
- **mod**: Calculate modulo (remainder)
- **|x|**: Calculate absolute value

### History
- View your recent calculations in the history panel
- History is automatically maintained (last 10 calculations)

## Project Structure

```
calculator-frontend/
├── public/
│   ├── index.html          # Main HTML template
│   └── manifest.json       # PWA manifest
├── src/
│   ├── App.js              # Main application component
│   ├── App.css             # Application styles
│   ├── index.js            # Application entry point
│   └── index.css           # Global styles
├── package.json            # Dependencies and scripts
└── README.md              # This file
```

## Available Scripts

- `npm start` - Start development server
- `npm test` - Run tests
- `npm run build` - Build for production
- `npm run eject` - Eject from Create React App (irreversible)

## Technologies Used

- **React**: Frontend framework
- **JavaScript (ES6+)**: Programming language
- **CSS3**: Styling
- **Create React App**: Build tool
- **React Hooks**: State management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.