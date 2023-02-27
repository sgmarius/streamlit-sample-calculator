import unittest
from app.components.logic import CalculatorLogic

class TestCalculatorLogic(unittest.TestCase):

    def test_logic(self):
        test_input = {
            "statistical_power": 0.80,
            "confidence_level": 0.95,
            "baseline_conversion_rate": .118,
            "lift": .05,
            "daily_visitors": 10000,
            "number_of_offers": 5
        }

        expected_output = {
            "statistical_power_threshold": .8416,
            "confidence_level_threashold": 1.96,
            "absolute_difference_conversion_rate": .0059,
            "rate_alternative": .1239,
            "daily_number_visitors_offer": 2000,
            "sample_size_offer_visitors": 47942,
            "sample_size_offer_conversion": 5657,
            "days_to_complete_test": 24,

        }

        calculator = CalculatorLogic(test_input)
        self.assertEqual(calculator.outputs, expected_output)


if __name__ == '__main__':
    unittest.main()