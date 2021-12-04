import os.path
import unittest

from day3.get_life_support_rating_part2 import get_life_support_rating
from day3.get_power_consumption_part1 import get_power_consumption


class TestPowerConsumption(unittest.TestCase):

    def test_part_1(self):
        test_input = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../test_input.txt')
        consumption = get_power_consumption(test_input)
        self.assertEqual(consumption, 198)

    def test_part_2(self):
        test_input = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../test_input.txt')
        consumption = get_life_support_rating(test_input)
        self.assertEqual(consumption, 230)