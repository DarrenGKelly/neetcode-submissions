class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i, num in enumerate(numbers):
            low, high = i + 1, len(numbers) - 1
            while low <= high:
                mid = (low + high) // 2
                if (numbers[mid] == target - num):
                    return [ i + 1 , mid + 1 ]
                elif (numbers[mid] < target - num):
                    low = mid + 1
                else:
                    high = mid - 1
                