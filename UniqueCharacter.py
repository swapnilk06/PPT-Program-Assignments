class Solution:
    def firstUniqChar(self, s: str) -> int:

        s1 = [i for i in "".join(s)]

        d = {}
        for i in s1:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        L = []
        for key,val in d.items():
            if val == 1:
                L.append(key)

        if len(L) == 0:
            return -1 
        else:
            s1 = s1.index(L[0])
            return s1
