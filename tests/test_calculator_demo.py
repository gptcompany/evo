"""
TDD Guard Demo - Calculator Test
Testing TDD workflow: RED → GREEN → REFACTOR
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_calculator_add():
    """Test addition function - should FAIL initially"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    result = calc.add(2, 3)
    assert result == 5


def test_calculator_multiply():
    """Test multiplication function - should FAIL initially"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    result = calc.multiply(4, 5)
    assert result == 20


def test_calculator_divide_by_zero():
    """Test division by zero handling - should FAIL initially"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_calculator_add_type_validation():
    """Test type validation for add method"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    with pytest.raises(TypeError, match="Parameter 'a' must be a number"):
        calc.add("not_a_number", 5)


def test_calculator_multiply_supports_floats():
    """Test that multiply works with floats"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    result = calc.multiply(2.5, 4.0)
    assert result == 10.0


def test_calculator_divide_returns_float():
    """Test that divide always returns float"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    result = calc.divide(10, 2)
    assert isinstance(result, float)
    assert result == 5.0