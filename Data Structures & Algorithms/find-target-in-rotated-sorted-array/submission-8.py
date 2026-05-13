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
            
        i_start = low
        end = False
        print(low, nums[low])

        if (target >= nums[i_start] and target <= nums[-1]):
            nums = nums[i_start:]
            end = True
        else:
            nums = nums[:i_start]
        
        print (nums)

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
        