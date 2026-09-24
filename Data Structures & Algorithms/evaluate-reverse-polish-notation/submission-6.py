class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        list1=[]
        for s in tokens:
            if s=="+":
                list1.append(list1.pop()+list1.pop())
            elif s=="*":
                list1.append(list1.pop()*list1.pop())
            elif s=="/":
                a,b=list1.pop(),list1.pop()
                list1.append(int(b/a))
            elif s=="-":
                a,b=list1.pop(),list1.pop()
                list1.append(b-a)
            else:
                list1.append(int(s))
        return list1[0]