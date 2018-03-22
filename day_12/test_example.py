from unittest import TestCase

from day_12.example import super_sum


class TestExample(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sum_one_plus_two_equals_three(self):
        # given
        a = 1
        b = 2
        expected = 3
        result = super_sum(a, b)
        self.assertEqual(result, expected)

    def test_sum_raises_valueerr_for_int_and_str(self):
        a = 'abc'
        b = 3
        with self.assertRaises(TypeError):
            super_sum(a, b)

    def test_sum_adds_any_number_of_numbers(self):
        data = [1, 2, 3]
        expected = 6
        result = super_sum(*data)
        self.assertEqual(result, expected)
