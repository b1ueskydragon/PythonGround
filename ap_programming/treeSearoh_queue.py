"""
BFS
"""
from queue import Queue

queue = Queue()
nums = reversed(sorted([10, 34, 55, 77]))

# TODO Not Using status, just stacking sum on a variable.

class Status:
    def __init__(self):
        self.total = 0
        self.selected_nums = []
        self.next = 1


class NextStatus:
    def __init__(self, s):
        self.total = s.total + nums[s.next]
        self.selected_nums = s.selected_nums + [s.next]
        if s.next is len(nums):
            self.next = 1
        else:
            self.next = s.next + 1


class NextNotStatus:
    def __init__(self, s):
        self.total = s.total
        self.selected_nums = s.selected_nums
        if s.next is len(nums):
            self.next = 1
        else:
            self.next = s.next + 1


def treeSearoh(target):
    curr_status = Status()  # 現在取得値
    ans_status = Status()  # 候補

    queue.put(curr_status)

    while not queue.empty():
        queue.get()
        if abs(target - ans_status.total) > abs(target - curr_status.total):
            ans_status = curr_status

        if curr_status.next and curr_status < target:
            next_status = NextStatus(curr_status)
            next_not_status = NextNotStatus(curr_status)
            queue.put(next_status)
            queue.put(next_not_status)
