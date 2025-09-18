"""
TDD Guard Demo - Test di Enforcement
Questo test dovrebbe far scattare TDD Guard
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


def test_new_feature_should_fail():
    """Test per nuova feature - deve fallire prima"""
    from src.calculator_demo import Calculator

    calc = Calculator()
    # Test per feature non ancora implementata
    result = calc.subtract(10, 3)
    assert result == 7