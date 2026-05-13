class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Binary Search for min value
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if (nums[mid] > nums[high]):
                low = mid + 1
            else:
                high = mid
        
        # Save lowest element's index
        i_start = low
        # Check which side of split target is in
        end = target >= nums[i_start] and target <= nums[-1]
        nums = nums[i_start:] if end else nums[:i_start]

        # Binary Search in the trimmed list
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if (nums[mid] == target):
                return mid + i_start if end else mid
            elif (nums[mid] <= target):
                low = mid + 1
            else:
                high = mid - 1

        return -1
        