def flight_itinerary(remains, journey):
    """
    :param remains: random-ordered itineraries
    :param journey: an list of itineraries
    :return: a completed journey (an list of whole itineraries which is ordered correctly)
    """
    if not remains:  # base case
        return journey

    last_stop = journey[-1]

    for i, (departure, arrival) in enumerate(remains):
        journey.append(arrival)
        if departure == last_stop:  # going deeper if only has valid itinerary
            return flight_itinerary(remains[:i] + remains[i + 1:], journey)
        else:
            journey.pop()  # cannot use

    return []  # if remains, the journey is incompleted.
