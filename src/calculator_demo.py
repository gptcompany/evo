"""
Calculator Demo - TDD Guard Test (Refactored)
Production-ready calculator with enhanced error handling and type safety.
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """
    Production-ready calculator with comprehensive error handling.

    Features:
    - Type-safe operations with Union[int, float]
    - Comprehensive error handling
    - Input validation
    - Extensive documentation
    """

    def add(self, a: Number, b: Number) -> Number:
        """
        Add two numbers with type validation.

        Args:
            a: First number (int or float)
            b: Second number (int or float)

        Returns:
            Sum of a and b

        Raises:
            TypeError: If inputs are not numbers
        """
        self._validate_number(a, "a")
        self._validate_number(b, "b")
        return a + b

    def multiply(self, a: Number, b: Number) -> Number:
        """
        Multiply two numbers with type validation.

        Args:
            a: First number (int or float)
            b: Second number (int or float)

        Returns:
            Product of a and b

        Raises:
            TypeError: If inputs are not numbers
        """
        self._validate_number(a, "a")
        self._validate_number(b, "b")
        return a * b

    def divide(self, a: Number, b: Number) -> float:
        """
        Divide two numbers with comprehensive validation.

        Args:
            a: Dividend (int or float)
            b: Divisor (int or float)

        Returns:
            Division result as float

        Raises:
            ValueError: If dividing by zero
            TypeError: If inputs are not numbers
        """
        self._validate_number(a, "a")
        self._validate_number(b, "b")

        if b == 0:
            raise ValueError("Cannot divide by zero")
        return float(a) / float(b)

    def subtract(self, a: Number, b: Number) -> Number:
        """
        Subtract two numbers with type validation.

        Args:
            a: Minuend (int or float)
            b: Subtrahend (int or float)

        Returns:
            Difference of a and b

        Raises:
            TypeError: If inputs are not numbers
        """
        self._validate_number(a, "a")
        self._validate_number(b, "b")
        return a - b

    def power(self, a: Number, b: Number) -> Number:
        """
        Raise a to the power of b with type validation.

        Args:
            a: Base number (int or float)
            b: Exponent (int or float)

        Returns:
            a raised to the power of b

        Raises:
            TypeError: If inputs are not numbers
        """
        self._validate_number(a, "a")
        self._validate_number(b, "b")
        return a ** b

    def sqrt(self, a: Number) -> float:
        """Calculate square root of a number."""
        return a ** 0.5

    def _validate_number(self, value: any, param_name: str) -> None:
        """
        Validate that a value is a number.

        Args:
            value: Value to validate
            param_name: Parameter name for error messages

        Raises:
            TypeError: If value is not a number
        """
        if not isinstance(value, (int, float)):
            raise TypeError(f"Parameter '{param_name}' must be a number, got {type(value).__name__}")