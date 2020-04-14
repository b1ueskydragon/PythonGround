class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        def divide(xs, l, r):
            if not xs:
                return xs
            if r - l == 0:
                return [xs[l]]
            if r - l == 1:
                a, b = xs[l], xs[r]
                return ([b, a], [a, b])[a < b]
            m = l + (r - l) // 2
            left = divide(xs, l, m)
            right = divide(xs, m + 1, r)
            # print(left, right)
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

        return divide(nums, 0, len(nums) - 1)
