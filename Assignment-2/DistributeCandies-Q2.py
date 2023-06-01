class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
    
    
        l = len(candyType)
        eat = l//2
        dis_candyType = set(candyType)

        if eat <= len(dis_candyType):
            return eat

        elif eat > len(dis_candyType):
            return len(dis_candyType) 
