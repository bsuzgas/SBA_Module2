import unittest
from app import calculate_total_cost, calculate_brake_pad_cost

class TestMaintenance(unittest.TestCase):
    def test_calculate_cost(self):
        # Verification: If parts are 1050 and labor is 700, total must be 1750
        self.assertEqual(calculate_total_cost(1050, 700), 1750)

if __name__ == "__main__":
    unittest.main()


def test_brake_pads(self):
    # Verification for brake pads
    self.assertEqual(calculate_brake_pad_cost(300, 250), 550)