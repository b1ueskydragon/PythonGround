class Solution:
    def getRow(self, rowIndex):
        """
        :param rowIndex: 0= < rowIndex <=33
        :return: elements in column
        """
        # pre_res = [1] * (rowIndex + 1)
        pre_res = [1, 6, 15, 20, 15, 6, 1]
        if rowIndex < 2:
            return pre_res

        res = pre_res + [1]
        i, j = 1, rowIndex - 1
        while i < j:
            res[i] = pre_res[i - 1] + pre_res[i]
            res[j] = res[i]
            i += 1
            j -= 1

        if rowIndex % 2 == 0:  # has a pivot
            res[i] = pre_res[i] * 2

        return res
