import React, { useState, useEffect, useCallback } from 'react';
import './App.css';

function App() {
  const [display, setDisplay] = useState('0');
  const [previousValue, setPreviousValue] = useState(null);
  const [operation, setOperation] = useState(null);
  const [waitingForOperand, setWaitingForOperand] = useState(false);
  const [history, setHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [backendStatus, setBackendStatus] = useState('checking');

  useEffect(() => {
    fetchHistory();
    checkBackendStatus();
  }, []);

  // Keyboard support
  useEffect(() => {
    const handleKeyPress = (event) => {
      const key = event.key;

      if (key >= '0' && key <= '9') {
        inputDigit(parseInt(key));
      } else if (key === '.') {
        inputDecimal();
      } else if (key === '+') {
        performOperation('add');
      } else if (key === '-') {
        performOperation('subtract');
      } else if (key === '*') {
        performOperation('multiply');
      } else if (key === '/') {
        performOperation('divide');
      } else if (key === 'Enter' || key === '=') {
        calculate();
      } else if (key === 'Escape' || key === 'c' || key === 'C') {
        clear();
      } else if (key === 'Backspace') {
        backspace();
      }
    };

    window.addEventListener('keydown', handleKeyPress);
    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [display, waitingForOperand, operation, previousValue]);

  const checkBackendStatus = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/health');
      if (response.ok) {
        setBackendStatus('online');
      } else {
        setBackendStatus('offline');
      }
    } catch (error) {
      setBackendStatus('offline');
    }
  };

  // For now, we'll simulate API calls to the Python backend
  // In a real implementation, you'd make HTTP requests to your Flask/FastAPI server

  const performCalculation = async (op, a, b = null) => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch('http://localhost:5000/api/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          operation: op,
          args: b !== null ? [a, b] : [a]
        })
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Calculation failed');
      }

      const data = await response.json();

      // Add to history
      const historyEntry = `${op}(${a}${b !== null ? `, ${b}` : ''}) = ${data.result}`;
      setHistory(prev => [historyEntry, ...prev.slice(0, 9)]); // Keep last 10 entries

      return data.result;
    } catch (error) {
      if (error.name === 'TypeError' && error.message.includes('fetch')) {
        // Fallback to mock calculation if backend is not running
        console.warn('Backend not available, using mock calculation');
        setBackendStatus('offline');
        return performMockCalculation(op, a, b);
      }
      setError(error.message);
      throw error;
    } finally {
      setIsLoading(false);
    }
  };

  const performMockCalculation = (op, a, b = null) => {
    // Fallback mock implementation
    let result;
    switch (op) {
      case 'add':
        result = a + (b || 0);
        break;
      case 'subtract':
        result = a - (b || 0);
        break;
      case 'multiply':
        result = a * (b || 1);
        break;
      case 'divide':
        if (b === 0) throw new Error('Cannot divide by zero');
        result = a / b;
        break;
      case 'power':
        result = Math.pow(a, b || 2);
        break;
      case 'sqrt':
        if (a < 0) throw new Error('Cannot take square root of negative number');
        result = Math.sqrt(a);
        break;
      case 'factorial':
        if (a < 0 || !Number.isInteger(a)) throw new Error('Factorial requires non-negative integer');
        result = factorial(a);
        break;
      case 'log':
        if (a <= 0) throw new Error('Logarithm requires positive number');
        result = Math.log10(a);
        break;
      case 'sin':
        result = Math.sin(a);
        break;
      case 'cos':
        result = Math.cos(a);
        break;
      case 'tan':
        result = Math.tan(a);
        break;
      case 'asin':
        if (a < -1 || a > 1) throw new Error('Arcsine input must be between -1 and 1');
        result = Math.asin(a);
        break;
      case 'acos':
        if (a < -1 || a > 1) throw new Error('Arccosine input must be between -1 and 1');
        result = Math.acos(a);
        break;
      case 'atan':
        result = Math.atan(a);
        break;
      case 'ln':
        if (a <= 0) throw new Error('Natural logarithm requires positive number');
        result = Math.log(a);
        break;
      case 'exp':
        result = Math.exp(a);
        break;
      case 'sinh':
        result = Math.sinh(a);
        break;
      case 'cosh':
        result = Math.cosh(a);
        break;
      case 'tanh':
        result = Math.tanh(a);
        break;
      case 'pi':
        result = Math.PI;
        break;
      case 'e':
        result = Math.E;
        break;
      default:
        throw new Error('Unknown operation');
    }

    // Add to history
    const historyEntry = `${op}(${a}${b !== null ? `, ${b}` : ''}) = ${result}`;
    setHistory(prev => [historyEntry, ...prev.slice(0, 9)]);

    return result;
  };

  const factorial = (n) => {
    if (n === 0 || n === 1) return 1;
    return n * factorial(n - 1);
  };

  const fetchHistory = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/history');
      if (!response.ok) {
        throw new Error('Failed to fetch history');
      }
      const data = await response.json();
      setHistory(data.history || []);
    } catch (error) {
      console.warn('Could not fetch history from backend:', error.message);
      // Keep existing history if backend is not available
    }
  };

  const clearHistory = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/history', {
        method: 'DELETE'
      });
      if (!response.ok) {
        throw new Error('Failed to clear history');
      }
      setHistory([]);
    } catch (error) {
      console.warn('Could not clear history on backend:', error.message);
      // Clear local history anyway
      setHistory([]);
    }
  };

  const inputDigit = (digit) => {
    if (waitingForOperand) {
      setDisplay(String(digit));
      setWaitingForOperand(false);
    } else {
      setDisplay(display === '0' ? String(digit) : display + digit);
    }
  };

  const inputDecimal = () => {
    if (waitingForOperand) {
      setDisplay('0.');
      setWaitingForOperand(false);
    } else if (display.indexOf('.') === -1) {
      setDisplay(display + '.');
    }
  };

  const clear = () => {
    setDisplay('0');
    setPreviousValue(null);
    setOperation(null);
    setWaitingForOperand(false);
    setError(null);
  };

  const clearDisplay = () => {
    setDisplay('0');
    setError(null);
  };

  const backspace = () => {
    if (display.length > 1) {
      setDisplay(display.slice(0, -1));
    } else {
      setDisplay('0');
    }
  };

  const performOperation = async (nextOperation) => {
    const inputValue = parseFloat(display);

    if (previousValue === null) {
      setPreviousValue(inputValue);
    } else if (operation) {
      try {
        const currentValue = previousValue || 0;
        const result = await performCalculation(operation, currentValue, inputValue);
        setDisplay(String(result));
        setPreviousValue(result);
      } catch (error) {
        setDisplay('Error');
        setPreviousValue(null);
      }
    }

    setWaitingForOperand(true);
    setOperation(nextOperation);
  };

  const performAdvancedOperation = async (op) => {
    const inputValue = parseFloat(display);
    try {
      let result;
      // Single argument operations
      if (op === 'sqrt' || op === 'factorial' || op === 'log' ||
          op === 'sin' || op === 'cos' || op === 'tan' ||
          op === 'asin' || op === 'acos' || op === 'atan' ||
          op === 'ln' || op === 'exp' || op === 'sinh' || op === 'cosh' || op === 'tanh' ||
          op === 'pi' || op === 'e') {
        result = await performCalculation(op, inputValue);
      } else {
        // For operations needing two operands, store the operation
        setPreviousValue(inputValue);
        setOperation(op);
        setWaitingForOperand(true);
        return;
      }
      setDisplay(String(result));
    } catch (error) {
      setDisplay('Error');
    }
  };

  const calculate = async () => {
    const inputValue = parseFloat(display);

    if (previousValue !== null && operation) {
      try {
        const result = await performCalculation(operation, previousValue, inputValue);
        setDisplay(String(result));
        setPreviousValue(null);
        setOperation(null);
        setWaitingForOperand(true);
      } catch (error) {
        setDisplay('Error');
        setPreviousValue(null);
        setOperation(null);
        setWaitingForOperand(true);
      }
    }
  };

  return (
    <div className="App">
      <div className="calculator-container">
        <div className="calculator-header">
          <h1>Advanced Calculator</h1>
          <div className={`backend-status ${backendStatus}`}>
            Backend: {backendStatus === 'online' ? '🟢 Online' : backendStatus === 'offline' ? '🔴 Offline' : '🟡 Checking...'}
          </div>
        </div>

        <div className={`calculator-display ${error ? 'error' : ''}`}>
          <div className="display-content">
            {isLoading ? (
              <div className="loading">Calculating...</div>
            ) : error ? (
              <div className="error-message">{error}</div>
            ) : (
              display
            )}
          </div>
        </div>

        <div className="calculator-buttons">
          {/* Row 1 */}
          <button className="btn btn-clear" onClick={clear} title="Clear All (C)">
            AC
          </button>
          <button className="btn btn-clear-display" onClick={clearDisplay} title="Clear Display">
            CE
          </button>
          <button className="btn btn-backspace" onClick={backspace} title="Backspace (⌫)">
            ⌫
          </button>
          <button className="btn btn-operator" onClick={() => performOperation('divide')} title="Divide (/)">
            ÷
          </button>

          {/* Row 2 */}
          <button className="btn btn-number" onClick={() => inputDigit(7)}>7</button>
          <button className="btn btn-number" onClick={() => inputDigit(8)}>8</button>
          <button className="btn btn-number" onClick={() => inputDigit(9)}>9</button>
          <button className="btn btn-operator" onClick={() => performOperation('multiply')} title="Multiply (*) or (×)">
            ×
          </button>

          {/* Row 3 */}
          <button className="btn btn-number" onClick={() => inputDigit(4)}>4</button>
          <button className="btn btn-number" onClick={() => inputDigit(5)}>5</button>
          <button className="btn btn-number" onClick={() => inputDigit(6)}>6</button>
          <button className="btn btn-operator" onClick={() => performOperation('subtract')} title="Subtract (-) or (−)">
            −
          </button>

          {/* Row 4 */}
          <button className="btn btn-number" onClick={() => inputDigit(1)}>1</button>
          <button className="btn btn-number" onClick={() => inputDigit(2)}>2</button>
          <button className="btn btn-number" onClick={() => inputDigit(3)}>3</button>
          <button className="btn btn-operator" onClick={() => performOperation('add')} title="Add (+) or (＋)">
            +
          </button>

          {/* Row 5 */}
          <button className="btn btn-number zero-btn" onClick={() => inputDigit(0)}>0</button>
          <button className="btn btn-number" onClick={inputDecimal} title="Decimal Point (.)">
            .
          </button>
          <button className="btn btn-equals" onClick={calculate} title="Calculate (=) or (Enter)">
            =
          </button>
        </div>

        <div className="advanced-buttons">
          <div className="button-row">
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('sqrt')} title="Square Root">
              √
            </button>
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('power')} title="Power (x^y)">
              xʸ
            </button>
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('factorial')} title="Factorial (n!)">
              n!
            </button>
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('log')} title="Logarithm (base 10)">
              log
            </button>
          </div>
          <div className="button-row">
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('percentage')} title="Percentage">
              %
            </button>
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('modulo')} title="Modulo">
              mod
            </button>
            <button className="btn btn-advanced" onClick={() => performAdvancedOperation('absolute')} title="Absolute Value">
              |x|
            </button>
            <button className="btn btn-refresh" onClick={checkBackendStatus} title="Check Backend Status">
              🔄
            </button>
          </div>
        </div>

        <div className="scientific-buttons">
          <div className="button-row">
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('sin')} title="Sine (radians)">
              sin
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('cos')} title="Cosine (radians)">
              cos
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('tan')} title="Tangent (radians)">
              tan
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('ln')} title="Natural Logarithm">
              ln
            </button>
          </div>
          <div className="button-row">
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('asin')} title="Arcsine (radians)">
              asin
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('acos')} title="Arccosine (radians)">
              acos
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('atan')} title="Arctangent (radians)">
              atan
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('exp')} title="Exponential (e^x)">
              eˣ
            </button>
          </div>
          <div className="button-row">
            <button className="btn btn-constant" onClick={() => performAdvancedOperation('pi')} title="Pi (π)">
              π
            </button>
            <button className="btn btn-constant" onClick={() => performAdvancedOperation('e')} title="Euler's number (e)">
              e
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('sinh')} title="Hyperbolic sine">
              sinh
            </button>
            <button className="btn btn-scientific" onClick={() => performAdvancedOperation('cosh')} title="Hyperbolic cosine">
              cosh
            </button>
          </div>
        </div>

        {history.length > 0 && (
          <div className="history-container">
            <div className="history-header">
              <h3 className="history-title">📜 Calculation History</h3>
              <button className="btn btn-clear-history" onClick={clearHistory} title="Clear History">
                🗑️ Clear
              </button>
            </div>
            <div className="history-list">
              {history.map((entry, index) => (
                <div key={index} className="history-item" title="Click to use result">
                  {entry}
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="keyboard-hint">
          💡 <strong>Keyboard Support:</strong> Use number keys, operators (+, -, *, /), Enter for =, Escape/C for clear, Backspace to delete
        </div>
      </div>
    </div>
  );
}

export default App;