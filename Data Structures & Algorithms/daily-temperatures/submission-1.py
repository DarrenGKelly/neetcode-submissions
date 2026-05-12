class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # stores indices

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than what's waiting on the stack
            while stack and temp > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx  # days waited
            stack.append(i)

        # Anything left in stack never found a warmer day, result stays 0
        return result
