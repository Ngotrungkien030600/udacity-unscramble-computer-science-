import unittest

class Task0Test(unittest.TestCase):
    """Task 0 unit test

    Args:
        unittest (object): The test case
    """
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
if __name__ == '__main__':
    unittest.main()