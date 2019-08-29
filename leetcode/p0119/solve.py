class Solution:
    def getRow(self, rowIndex):
        """
        getRow recursively.

        :param rowIndex: 0 =< rowIndex <= 33
        :return: list of elements in the column
        """
        if rowIndex < 2:
            return self.pascal(rowIndex, [1] * (rowIndex + 1))
        return self.pascal(rowIndex, self.getRow(rowIndex - 1))

    def pascal(self, row_index, pre_res):
        """
        two cursors move from both end at the same time.
        extra O(k) space (res) required.

        :param row_index: k
        :param pre_res: previous result
        :return: current result
        """
        if row_index < 2:
            return pre_res

        res = pre_res + [1]
        i, j = 1, row_index - 1
        while i < j:
            res[i] = pre_res[i - 1] + pre_res[i]
            res[j] = res[i]
            i += 1
            j -= 1

        if row_index % 2 == 0:  # has a pivot
            res[i] = pre_res[i] * 2

        return res
