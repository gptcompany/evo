import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_sqrt_simple():
    """Test basic square root functionality"""
    from src.calculator_demo import Calculator
    calc = Calculator()
    result = calc.sqrt(4)
    assert result == 2.0  # More precise assertion