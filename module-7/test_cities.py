import unittest
from city_functions import city_country

class city_country_testcase(unittest.TestCase):

    def test_city_country(self):
        formatted_city_name = city_country("Tegucigalpa", "Honduras")
        self.assertEqual(formatted_city_name, "Tegucigalpa, Honduras")

if __name__ == "__main__":
    unittest.main()
