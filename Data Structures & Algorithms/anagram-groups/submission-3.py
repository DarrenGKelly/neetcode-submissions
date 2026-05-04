class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = []
        for word in strs:
            found = False
            for group in groups:
                if (sorted(word) == sorted(group[0])):
                    group.append(word)
                    found = True
                    break
            
            if not found:
                groups.append([word])
        
        return groups