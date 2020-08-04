

class Solution:
    def isHappy(self, n: int) -> bool:
        strn= str(n)
        total=0
        d={}
        while True:
            for i in range(len(strn)):
                total+=int(strn[i])**2
            print(total)
            if total==1:                
                return True
            else:
                strn=str(total)
                if total in d:
                    return False
                else:
                    d[total]=total
            total=0
                
            
        
