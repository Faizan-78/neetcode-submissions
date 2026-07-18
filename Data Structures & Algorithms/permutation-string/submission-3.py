class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        freq2 = {}
        n = len(s1)
        for char in s1:
            freq1[char] = freq1.get(char,0) + 1
        
        l = 0
        
        for r in range(len(s2)):
            freq2[s2[r]] = freq2.get(s2[r],0) + 1
            if (r - l +1) > n:
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                  del freq2[s2[l]]
                l += 1
            if r - l + 1 == n:
                if freq1 == freq2: 
                 return True
        return False
         
            
