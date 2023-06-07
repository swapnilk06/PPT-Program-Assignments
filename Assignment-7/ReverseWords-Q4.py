class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([s_[::-1] for s_ in s.split(" ")])
