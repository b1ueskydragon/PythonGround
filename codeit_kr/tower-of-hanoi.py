def move_disk(disks, left, right):
    print("move disk %d, from %d to %d" % (disks, left, right))


def hanoi(num_discs, start_peg, end_peg):
    """
    print out order of discs moving.

    :param num_discs: number of discs (1 is smallest. 1, 2, .., num_discs)
    :param start_peg: index of start peg (1, 2, 3)
    :param end_peg: index of goal peg (1, 2, 3)
    """

    # edge case
    if num_discs < 1:
        return

    if num_discs == 1:
        move_disk(num_discs, 1, 3)

    hanoi(num_discs - 1, start_peg, end_peg)
    inter_peg = 6 - start_peg - end_peg
    move_disk(num_discs, start_peg, inter_peg)


# test
# hanoi(1, 1, 3)
# hanoi(2, 1, 3)

hanoi(3, 1, 3)

# TODO: gray code
