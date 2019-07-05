class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num not in dict1:
                dict1[nums[i]] = i
            else:
                return [dict1[num], i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 6, 5], 7))