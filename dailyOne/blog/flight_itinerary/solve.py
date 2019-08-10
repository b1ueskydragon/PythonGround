def get_itinerary(flights: [(str, str)], itinerary: [str]) -> [str]:
    """
    Backtracking (pruning before dive into recursion).

    :param flights: pair of departure and destination
    :param itinerary: result (destinations)
    :return: result (destinations)
    """
    if not flights:  # base case
        return itinerary

    last_stop = itinerary[-1]  # goal

    for i, flight in enumerate(flights):
        start, stop = flight
        itinerary.append(stop)
        flights_not_used = flights[:i] + flights[i + 1:]
        if last_stop == start:
            return get_itinerary(flights_not_used, itinerary)
        itinerary.pop()
