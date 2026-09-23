class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeToOpen={")":"(","]":"[","}":"{"}
        for c in s:
            if c not in closeToOpen:
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                popped=stack.pop()
                if popped!=closeToOpen[c]:
                    return False
        return len(stack)==0
