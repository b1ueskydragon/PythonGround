class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        def divide(xs):
            if len(xs) < 2:
                return xs
            mid = len(xs) // 2
            left = divide(xs[:mid])
            right = divide(xs[mid:])
            return conquer(left, right)

        def conquer(l1, l2):
            # l1, l2 = sorted list
            merged = []
            while l1 and l2:
                if l1[0] < l2[0]:
                    merged.append(l1.pop(0))
                else:
                    merged.append(l2.pop(0))
            merged += l1
            merged += l2
            return merged

        return divide(nums)
