class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack=[]
        stack2=[]
        for i in range(len(S)):
            if S[i]=='#' and len(stack)>0:
                stack.pop()
            if S[i]!='#':
                stack.append(S[i])
        for j in range(len(T)):
            if T[j]=='#' and len(stack2)>0:
                stack2.pop()
            if T[j]!='#':
                stack2.append(T[j])
        
        print(stack)
        print(stack2)
        if stack==stack2:
            return True
        else:
            return False
