from unittest import TestCase
from lesson6_OOP_unittest.unittests.unittest_1 import Calculator


class TestCalculator(TestCase):
    def test_add(self):
         # calculator = Calculator()

         self.assertEqual(Calculator().add(2,3),5)
         self.assertEqual(Calculator().add(2, 3), 4)

         # self.assertEqual(5, Calculator().add(2, 3))
         # self.assertEqual(4, Calculator().add(2, 3))
