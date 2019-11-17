import unittest

from retrospective.flight_itinerary import flight_itinerary


class GetItineraryTest(unittest.TestCase):
    def test_get_itinerary_simplify(self):
        flights = [["C", "D"], ["B", "C"], ["A", "B"]]
        curr = ["A"]
        expected = ["A", "B", "C", "D"]
        self.assertEqual(expected, flight_itinerary(flights, curr))

    def test_still_flights_remaining_simplify(self):
        flights = [["C", "D"], ["B", "C"], ["A", "B"]]
        curr = ["B"]
        expected = None  # ["A", "B"] is remaining, we must use all flights.
        self.assertEqual(expected, flight_itinerary(flights, curr))

    def test_no_flights_leaving_from_simplify(self):
        flights = [["C", "D"], ["B", "C"], ["A", "B"]]
        curr = ["D"]
        expected = None
        self.assertEqual(expected, flight_itinerary(flights, curr))

    def test_get_itinerary(self):
        flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
        curr = ["YUL"]
        expected = ["YUL", "ORD", "SFO", "HNL", "AKL"]
        self.assertEqual(expected, flight_itinerary(flights, curr))

    def test_still_flights_remaining(self):
        flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
        curr = ["ORD"]
        expected = None
        self.assertEqual(expected, flight_itinerary(flights, curr))

    def test_no_flights_leaving_from(self):
        flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
        curr = ["AKL"]
        expected = None
        self.assertEqual(expected, flight_itinerary(flights, curr))


if __name__ == '__main__':
    unittest.main()
