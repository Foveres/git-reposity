# 折半查找：递归实现和非递归实现


def bi_search_r(nums, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            mid = bi_search_r(nums, mid+1, right, target)
        elif nums[mid] == target:
            return mid
        else:
            mid = bi_search_r(nums, left, mid-1, target)
        return mid
    else:
        return -1


def bi_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid -1
        else:
            return mid
    return -1


if __name__=='__main__':
    nums = [5, 13, 19, 21, 37, 56, 64, 75, 80, 88, 92]
    position = bi_search_r(nums, 0, len(nums)-1, 75)
    position1 = bi_search(nums, 75)
    print(position)
    print(position1)

