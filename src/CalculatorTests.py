import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('csvFiles/addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = CsvReader('csvFiles/subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = CsvReader('csvFiles/multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(int(row['Value 1']), int(row['Value 2'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = CsvReader('csvFiles/division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(int(row['Value 1']), int(row['Value 2'])), format(float(row['Result']), '.7f'))
            self.assertEqual(self.calculator.result, format(float(row['Result']), '.7f'))

    def test_square(self):
        test_data = CsvReader('csvFiles/square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(int(row['Value 1'])), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_root(self):
        test_data = CsvReader('csvFiles/squareRoot.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square_root(int(row['Value 1'])), format(float(row['Result']), '.7f'))
            self.assertEqual(self.calculator.result, format(float(row['Result']), '.7f'))

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)


if __name__ == '__main__':
    unittest.main()
