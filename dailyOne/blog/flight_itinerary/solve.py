def get_itinerary(flights: [(str, str)], current_itinerary: [str]) -> [str]:
    """
    Backtracking (pruning before dive into recursion).

    :param flights: pair of departure and destination
    :param current_itinerary: result (destinations)
    :return: result (destinations)
    """
    if not flights:  # base case
        return current_itinerary

    last_stop = current_itinerary[-1]  # goal

    for i, flight in enumerate(flights):
        start, stop = flight
        current_itinerary.append(stop)
        flights_not_used = flights[:i] + flights[i + 1:]
        if last_stop == start:
            return get_itinerary(flights_not_used, current_itinerary)
        current_itinerary.pop()

    return current_itinerary
