"""
move all disks at least (2^n − 1) times
"""


def move_disk(disks, left, right):
    print(f"move disk {disks}, from {left} to {right}")


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

    inter_peg = 6 - start_peg - end_peg

    # move all disks except biggest one (standard pattern)
    hanoi(num_discs - 1, start_peg, inter_peg)

    # move biggest one to goal first
    move_disk(num_discs, start_peg, end_peg)

    # move remain disks to goal
    hanoi(num_discs - 1, inter_peg, end_peg)


# test
hanoi(1, 1, 3)
print()
hanoi(2, 1, 3)
print()
hanoi(3, 1, 3)

# TODO: gray code
