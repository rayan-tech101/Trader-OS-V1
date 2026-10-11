"""Basic tests for Trader OS V1"""

import sys

import pytest


class TestBasic:
    """Basic test suite to verify pytest setup and Python environment."""

    def test_python_version(self):
        """Test that Python 3.9+ is being used."""
        assert sys.version_info >= (3, 9), f"Python 3.9+ required, got {sys.version_info}"

    def test_pytest_available(self):
        """Test that pytest is installed and working."""
        assert pytest is not None
        assert hasattr(pytest, "main")

    def test_basic_assertion(self):
        """Test basic assertion functionality."""
        assert True is True
        assert 1 + 1 == 2


@pytest.mark.unit
def test_imports():
    """Test that standard library imports work."""
    import json
    import os
    import sys

    assert json is not None
    assert os is not None
    assert sys is not None


@pytest.mark.unit
def test_placeholder():
    """Placeholder test to ensure test discovery works."""
    result = True
    assert result is True
