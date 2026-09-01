# test_cryptoapidiamond.py
"""
Tests for CryptoAPIDiamond module.
"""

import unittest
from cryptoapidiamond import CryptoAPIDiamond

class TestCryptoAPIDiamond(unittest.TestCase):
    """Test cases for CryptoAPIDiamond class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoAPIDiamond()
        self.assertIsInstance(instance, CryptoAPIDiamond)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoAPIDiamond()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
