from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        for ts, val in self.timemap[key][::-1]:
            if ts <= timestamp:
                return val
        
        return ""
        
