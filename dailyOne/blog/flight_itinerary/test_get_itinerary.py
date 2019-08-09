import unittest

from dailyOne.blog.flight_itinerary.solve import get_itinerary


class GetItineraryTest(unittest.TestCase):
    def test_get_itinerary(self):
        flights = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")]
        expected = ["YUL", "ORD", "SFO", "HNL", "AKL"]
        current_itinerary = ["YUL"]  # departure
        self.assertEqual(expected, get_itinerary(flights, get_itinerary(flights, current_itinerary)))

    def test_return_none(self):
        flights = [("HNL", "AKL"), ("YUL", "ORD"), ("ORD", "SFO"), ("SFO", "HNL")]
        expected = []
        current_itinerary = ["AKL"]  # departure
        self.assertEqual(expected, get_itinerary(flights, get_itinerary(flights, current_itinerary)))


if __name__ == '__main__':
    unittest.main()
