# test_cryptointerceptor.py
"""
Tests for CryptoInterceptor module.
"""

import unittest
from cryptointerceptor import CryptoInterceptor

class TestCryptoInterceptor(unittest.TestCase):
    """Test cases for CryptoInterceptor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoInterceptor()
        self.assertIsInstance(instance, CryptoInterceptor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoInterceptor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
