"""
TDD Guard Test - Power Function
Test singolo per verificare enforcement dopo restart
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_calculator_power():
    """Test power function - deve fallire perché non esiste ancora"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    result = calc.power(2, 3)
    assert result == 8