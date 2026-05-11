class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i, num1 in enumerate(nums):
            for j_idx, num2 in enumerate(nums[i+1:]):
                j = j_idx + i + 1
                target = -(num1 + num2)

                # Binary search
                low, high = j + 1, len(nums) - 1
                while low <= high:
                    mid = (low + high) // 2
                    if (nums[mid] == target):
                        newTriplet = tuple(sorted([num1, num2, nums[mid]]))
                        triplets.add(newTriplet)
                        break
                    elif (nums[mid] < target):
                        low = mid + 1
                    else:
                        high = mid - 1

        return [list(t) for t in triplets]