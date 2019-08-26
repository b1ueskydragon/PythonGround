class Solution:
    def getRow(self, rowIndex):
        """
        :param rowIndex: 0= < rowIndex <=33
        :return: elements in column
        """
        res = self.pascal(rowIndex, [1] * (rowIndex + 1))
        for i in range((rowIndex + 1) // 2):
            res[-1 - i] = res[i]
        return res

    def pascal(self, k, res):
        if k < 2:
            return res
        for i in range((k + 1) // 2):
            res[i + 1] = res[i] + res[i + 1]
        return self.pascal(k - 1, res)
