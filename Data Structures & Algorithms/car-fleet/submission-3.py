class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        paired = sorted(zip(position, speed), reverse=True)
        position_s, speed_s = zip(*paired)

        for i in range(len(position_s)):

            if (fleets and (target - position_s[i]) / speed_s[i] <= (target - position_s[fleets[-1]]) / speed_s[fleets[-1]]):
                continue
            else:
                fleets.append(i)
        
        return len(fleets)