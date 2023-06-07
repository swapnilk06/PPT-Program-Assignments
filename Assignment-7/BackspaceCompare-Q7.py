class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.evaluate(s) == self.evaluate(t)

    def evaluate(self, str):
        stack = []
        for s in str:
            if s != "#":
                stack.append(s)
            elif stack:
                stack.pop()
        return stack
