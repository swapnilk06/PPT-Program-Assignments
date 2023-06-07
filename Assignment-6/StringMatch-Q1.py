class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        per=[]
        lower=0
        upper=len(s)
        for i in s:
            if i=='I':
                per.append(lower)
                lower+=1
            else:
                per.append(upper)
                upper-=1
        if s[len(s)-1]=='I':
            per.append(upper)
        else:
            per.append(lower)
        return per

            
