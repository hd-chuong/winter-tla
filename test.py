class Solution:
    def countUnique(self, s: str) -> int:
      
    	unique = set()
        for i in range(len(s)):
                unique.add(s[i])
        return len(unique)
    
    def longestSubstring(self, s: str, k: int) -> int:
	    maxUnique = self.countUnique(s)
      
        freq = {} # dict - hashmap
        res = 0
        for currUnique in range(maxUnique):
            left = 0
            right = 0
            count = 0 # count unique
                
            while left <= right and right < len(s):
                
                if count > currUnique:
                freq[s[left]] -= 1
                left += 1
                continue
                
                if s[right] in freq:
                freq[s[right]] += 1
                
                if s[right] not in freq:
                freq[s[right]] = 1
                count += 1
                
                            countK = 0
                # O(26 * N) ~ O(N)
                # freq <= 26
                for key in freq:
                if freq[key] >= k:
                    countK += 1
                
                if countK == currUnique:
                res = max(res, right -left + 1)
                
                right += 1
            
            return res