#!/usr/bin/env python3
"""Example test to verify TDD Guard integration."""

def test_basic_example():
    """A basic test to verify pytest is working."""
    assert 1 + 1 == 2

def test_string_operations():
    """Test string operations."""
    text = "hello world"
    assert text.upper() == "HELLO WORLD"
    assert len(text) == 11

def test_list_operations():
    """Test list operations."""
    numbers = [1, 2, 3, 4, 5]
    assert sum(numbers) == 15
    assert max(numbers) == 5
    assert min(numbers) == 1