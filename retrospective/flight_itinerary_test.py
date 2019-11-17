import unittest

from retrospective.flight_itinerary import flight_itinerary


class FlightItineraryTest(unittest.TestCase):
    def test_get_itinerary_simplify(self):
        flights = [["C", "D"], ["B", "C"], ["A", "B"]]
        journey = ["A"]
        expected = ["A", "B", "C", "D"]
        self.assertEqual(expected, flight_itinerary(flights, journey))

    def test_still_flights_remaining_simplify(self):
        flights = [["C", "D"], ["B", "C"], ["A", "B"]]
        journey = ["B"]
        expected = []  # ["A", "B"] is remaining, we must use all flights.
        self.assertEqual(expected, flight_itinerary(flights, journey))

    def test_no_flights_leaving_from_simplify(self):
        flights = [["C", "D"], ["B", "C"], ["A", "B"]]
        journey = ["D"]
        expected = []
        self.assertEqual(expected, flight_itinerary(flights, journey))

    def test_get_itinerary(self):
        flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
        journey = ["YUL"]
        expected = ["YUL", "ORD", "SFO", "HNL", "AKL"]
        self.assertEqual(expected, flight_itinerary(flights, journey))

    def test_still_flights_remaining(self):
        flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
        journey = ["ORD"]
        expected = []
        self.assertEqual(expected, flight_itinerary(flights, journey))

    def test_no_flights_leaving_from(self):
        flights = [["HNL", "AKL"], ["YUL", "ORD"], ["ORD", "SFO"], ["SFO", "HNL"]]
        journey = ["AKL"]
        expected = []
        self.assertEqual(expected, flight_itinerary(flights, journey))


if __name__ == '__main__':
    unittest.main()
