class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if (low == high or (nums[mid] < nums[mid + 1] and nums[mid] < nums[mid - 1])):
                return nums[mid]
            elif (nums[mid] < nums[high]):
                high = mid - 1
            else:
                low = mid + 1