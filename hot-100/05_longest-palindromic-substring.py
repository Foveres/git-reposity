
class Solution_01:
    def longestPalindorm(self, s):

        size = len(s)
        if size == 0:
            return

        lo_pal = 1
        lo_pal_str = s[0]
        for i in range(size):
            pal_odd, odd_len = self.__center_spread(s, size, i, i)
            pal_even, even_len = self.__center_spread(s, size, i, i+1)
            if odd_len >= even_len:
                cur_max_sub = pal_odd
            else:
                cur_max_sub = pal_even
            # cur_max_sub = pal_odd if odd_len >= even_len else pal_even

            if len(cur_max_sub) > lo_pal:
                lo_pal = len(cur_max_sub)
                lo_pal_str = cur_max_sub
        return lo_pal_str

    def __center_spread(self, s, size, left, right):
        while left >= 0 and right < size and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right], right-left-1


class Solution_02:
    def longestPalindorm(self, s):
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res



if __name__ == '__main__':
        solution_01 = Solution_01()
        print(solution_01.longestPalindorm('babad'))

        solution_02 = Solution_02()
        print(solution_02.longestPalindorm('babad'))