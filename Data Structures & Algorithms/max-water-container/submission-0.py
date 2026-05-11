class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0

        for i, height1 in enumerate(heights):
            for j_idx, height2 in enumerate(heights[i+1:]):
                j = j_idx + i + 1

                maxArea = max(maxArea, min(height1, height2) * (j - i))
        
        return maxArea