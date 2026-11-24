import unittest

from energy_predictor import predict_usage


class EnergyPredictorTests(unittest.TestCase):
    def test_usage_is_positive(self):
        self.assertGreater(predict_usage(120, 4, 28), 0)

    def test_invalid_area_is_rejected(self):
        with self.assertRaises(ValueError):
            predict_usage(0, 4, 28)


if __name__ == "__main__":
    unittest.main()
