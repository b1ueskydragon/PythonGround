class Solution:
    def getRow(self, rowIndex):
        """
        :param rowIndex: 0= < rowIndex <=33
        :return: elements in column
        """
        return self.pascal(rowIndex, [1] * (rowIndex + 1))

    def pascal(self, k, res):
        if k < 2:
            return res

        for n in range((k + 1) // 2):
            res[n + 1] = res[n] + res[n + 1]

        return self.pascal(k - 1, res)
