import unittest

# --- PART 1: THE ACTUAL CODE ( The Application ) ---
def add(x, y):
    return x - y

def multiply(x, y):
    return x * y

# --- PART 2: THE AUTOMATED TESTS ( What Jenkins will check ) ---
class TestCalculator(unittest.TestCase):
    
    # Test 1: Check if addition works
    def test_addition(self):
        result = add(10, 5)
        self.assertEqual(result, 15) # If 10+5 is not 15, this fails

    # Test 2: Check if multiplication works
    def test_multiplication(self):
        result = multiply(3, 4)
        self.assertEqual(result, 12) # If 3*4 is not 12, this fails

# --- ENTRY POINT ---
if __name__ == '__main__':
    # When this file is run, it triggers the tests automatically
    unittest.main()
