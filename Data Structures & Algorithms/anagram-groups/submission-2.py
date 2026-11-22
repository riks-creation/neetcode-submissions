class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            letter_count = [0] * 26
            for letter in string:
                letter_count[ord(letter) - ord("a")] += 1
            key = tuple(letter_count)
            if key in groups:
                groups[key].append(string)
            else: 
                groups[key] = [string]
        return list(groups.values())
            
        
        