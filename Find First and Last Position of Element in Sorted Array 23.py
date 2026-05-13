nums = [5,7,7,8,8,10]
target = 8
def searchRange(nums, target):
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left_index = findLeft(nums, target)
    right_index = findRight(nums, target)

    if left_index <= right_index and right_index < len(nums) and nums[left_index] == target and nums[right_index] == target:
        return [left_index, right_index]
    return [-1, -1] 