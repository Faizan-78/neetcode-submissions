class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       dict = { ")":"(" , "]" : "[", "}" :"{"}
       for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack or stack[-1] != dict[ch]:
                return False
            stack.pop()
       return not stack
        
