import logging
from typing import Optional

# Set up logging
logging.basicConfig(level=logging.INFO)

def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def divide(a: int, b: int) -> float:
    """Divide a by b, raise error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def safe_divide(a: int, b: int) -> Optional[float]:
    """Safely divide two numbers, with error handling."""
    try:
        return divide(a, b)
    except ValueError as e:
        logging.error(f"Error: {e}")
        return None  # Handle accordingly

if __name__ == "__main__":
    try:
        result = safe_divide(10, 0)  # Example usage with error handling
        if result is not None:
            logging.info(f"Result: {result}")
    except Exception as e:
        logging.exception("An unexpected error occurred.")
