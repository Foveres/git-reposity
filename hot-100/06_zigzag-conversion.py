class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s

        s_Rows = [""] * numRows
        i = 0
        n = len(s)
        while i < n:

            for j in range(numRows):
                if i < n:
                    s_Rows[j] += s[i]
                    i += 1

            for j in range(numRows-2, 0, -1):
                if i < n:
                    s_Rows[j] += s[i]
                    i += 1
        return "".join(s_Rows)


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert('LEETCODEISHIRING', 4))