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
        # TODO pruning
        # TODO recursion in for loop
        return get_itinerary(flights, current_itinerary)

    return current_itinerary
