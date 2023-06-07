class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        res = ''
        carry = 0
        while num1 and num2:
            x = int(num1.pop())
            y = int(num2.pop())
            digit = (x+y+carry) % 10
            carry = (x+y+carry) // 10
            res = str(digit) + res
        num1 = num1 if num1 else num2
        while num1 or carry:
            x = int(num1.pop()) if num1 else 0
            digit = (x+carry) % 10
            carry = (x+carry) // 10
            res = str(digit) + res
        return res
