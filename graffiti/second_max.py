def second_max(xs):
    fmax = max(xs[0], xs[1])
    smax = min(xs[0], xs[1])
    for i in range(2, len(xs)):
        if xs[i] > fmax:
            smax = fmax
            fmax = xs[i]
        elif xs[i] > smax:  # still smaller than current first max.
            smax = xs[i]
    return smax
