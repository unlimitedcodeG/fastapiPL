import unittest
from my_module import * 


class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-1,1),0)
    

    def test_subtract(self):
        self.assertEqual(subtract(3,2),1)
        self.assertEqual(subtract(3,3),0)


    
    def test_multiply(self):
        self.assertEqual(multiply(3, 2), 6)
        self.assertEqual(multiply(-1, 3), -3)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == '__main__':
    unittest.main()