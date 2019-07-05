class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        '.' 匹配任意单个字符
        '*' 匹配零个或多个前面的那一个元素
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('aa', 'a'))
    print(solution.isMatch('aa', 'a*'))
    print(solution.isMatch('ab', '.*'))
    print(solution.isMatch('aab', 'c*a*b'))
    print(solution.isMatch('mississippi', 'mis*is*p*.'))