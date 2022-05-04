import unittest
#EX1

def convert(f, target='c'):
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')

print(convert(50,'k'))
class TestConverter(unittest.TestCase):
    """
    This class will allow the user to convert the temperature in Fahrenheit degrees to Celsius degrees or Kelvins, depending on target parameter..
    """

    # EX2
    def test_convert_fahrenheit_to_celcius(self):
        self.assertEqual(convert(50, 'c'), 10)
        self.assertEqual(
            convert(70, 'c'), 21.11111111111111
        )
        self.assertEqual(
            convert(90, 'c'), 32.22222222222222
        )
    # EX3
    def test_correct_target_parameter(self):
        self.assertEqual(convert(50, "c"), 10)
        self.assertEqual(convert(50, "k"), 283.15)
        self.assertEqual(convert(50, "reaumur"), 10)



    # EX4
    def test_convert_fahrenheit_to_kelvin(self):
        self.assertEqual(
            convert(-500, "k"), -22.405555555555566
        )
        self.assertEqual(convert(0, "k"), 255.3722222222222)
        self.assertEqual(
            convert(1000, "k"), 810.9277777777777
        )




if __name__ == "__main__":
    unittest.main()
