class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict1 = defaultdict(int)

        for char in s:
            dict1[char] += 1
        for char in t:
            dict1[char] -= 1

        return all(v == 0 for v in dict1.values())        