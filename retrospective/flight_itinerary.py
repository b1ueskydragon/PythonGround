def flight_itinerary(remains, journey):
    """
    :param remains: random-ordered itineraries
    :param journey: an list of itineraries
    :return: a completed journey (an list of whole itineraries which is ordered correctly)
    """
    if not remains:  # base case
        return journey
