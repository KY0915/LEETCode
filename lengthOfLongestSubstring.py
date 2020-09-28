class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        d={}
        j=0
        m=0
        lm=0
        while(i<len(s) and j < len(s)):            
            if s[j] not in d:
                d[s[j]]=s[j]
                j+=1
                lm=len(d)
                if (m< lm):
                    m=lm                
            else:

                d.pop(s[i])
                i+=1
        return m
    def lengthOfLongestSubstring2(self, s: str) -> int:
        i=0
        d={}
        j=0
        m=0
        lm=0
        for j in range(len(s)):
            if s[j] in d:                                
                i=max(d[s[j]],i)
            m = max(m, j-i+1)
            d[s[j]]=j+1
    
        return m
        
        
