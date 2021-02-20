import unittest
from datetime import datetime
from domain_expiry import convert_to_datetime


class TestDomainExpiry(unittest.TestCase):

    def test_convert_to_datetime(self):
        regular_date = '2021-07-23T00:00:00'
        self.assertIs(type(
            convert_to_datetime(regular_date)), datetime)
        date_with_z = '2021-12-16T11:57:45Z'
        self.assertIs(type(convert_to_datetime(date_with_z)), datetime)

        date_with_offset = '2021-07-23T00:00:00-0700'
        self.assertIs(type(
            convert_to_datetime(date_with_offset)), datetime)
        date_with_offset = '2021-07-23T00:00:00-07:00'
        self.assertIs(type(
            convert_to_datetime(date_with_offset)), datetime)


if __name__ == '__main__':
    unittest.main()
