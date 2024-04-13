import unittest
from unittest.mock import patch
from factorial import factorial, main
from io import StringIO

class TestFactorial(unittest.TestCase):
    
    def test_factorial_of_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_negative_number_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)
            
    def test_factorial_of_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_of_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-5)
                    
    def test_factorial_of_two(self):
        self.assertEqual(factorial(2), 2)

    def test_factorial_of_large_negative_number(self):
        with self.assertRaises(ValueError):
            factorial(-100)
            
    def test_factorial_of_three(self):
        self.assertEqual(factorial(3), 6)
        
    def test_float_input(self):
        with self.assertRaises(ValueError):
            factorial(5.5)

    def test_small_number(self):
        result = factorial(0)
        self.assertEqual(result, 1)

    def test_non_numeric_string_input(self):
        with self.assertRaises(ValueError):
            factorial("abc") 
            
    @patch('sys.stdin', StringIO("5\n"))
    def test_main_with_valid_input(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(main(), 0)
            self.assertEqual(fake_out.getvalue().strip(), '120')

    @patch('sys.stdin', StringIO("abc\n"))
    def test_main_with_invalid_input(self):
        with patch('sys.stderr', new=StringIO()) as fake_err:
            self.assertEqual(main(), 1)
            self.assertIn("invalid literal for int()", fake_err.getvalue().strip())

    @patch('sys.stdin', StringIO("5 6 7\n"))
    def test_main_with_multiple_numbers(self):
        with patch('sys.stderr', new=StringIO()) as fake_err:
            self.assertEqual(main(), 1)
            self.assertIn("invalid literal for int()", fake_err.getvalue().strip())

if __name__ == "__main__":
    unittest.main()
