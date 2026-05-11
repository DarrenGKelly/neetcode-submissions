class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if (len(nums) == 0):
            return 0

        nums.sort()
        sequence = [nums[0]]
        maxSize = 1

        for num in nums[1:]:
            if (sequence[-1] == num - 1):
                sequence.append(num)
                maxSize = max(maxSize, len(sequence))
            elif (sequence[-1] == num):
                continue
            else:
                sequence = [num]


        return maxSize
        