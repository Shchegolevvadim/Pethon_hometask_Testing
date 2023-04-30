import unittest

class TestCaseName(unittest.TestCase):
    def test_method(self):
        self.assertEqual(5 * 6, 30, msg='Видимо и в этой вселенной не работает :-(')


if __name__=='__main__':
    unittest.main(verbosity=2)