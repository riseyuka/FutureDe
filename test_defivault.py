# test_defivault.py
"""
Tests for DeFiVault module.
"""

import unittest
from defivault import DeFiVault

class TestDeFiVault(unittest.TestCase):
    """Test cases for DeFiVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DeFiVault()
        self.assertIsInstance(instance, DeFiVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DeFiVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
