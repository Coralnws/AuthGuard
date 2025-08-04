# test_authguard.py
"""
Tests for AuthGuard module.
"""

import unittest
from authguard import AuthGuard

class TestAuthGuard(unittest.TestCase):
    """Test cases for AuthGuard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AuthGuard()
        self.assertIsInstance(instance, AuthGuard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AuthGuard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
