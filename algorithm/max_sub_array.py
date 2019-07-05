class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        for i in range(1, length):
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            print(nums[i])
            print(nums[i-1])
            subMaxSum=max(nums[i]+nums[i-1],nums[i])
            nums[i]=subMaxSum # 将当前和最大的赋给nums[i]，新的nums存储的为和值
        print(nums)
        return max(nums)


if __name__ == '__main__':
    solution = Solution()
    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)

