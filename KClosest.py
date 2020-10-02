class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        

        l=[]    
        for i in points:
            distance=pow((pow(i[0],2)+pow(i[1],2)),1/2)
            l.append(distance)
        
        l2=[]
        ks= heapq.nsmallest(K,l)[-1]
        print(ks)
        
        for i in points:
            distance=pow((pow(i[0],2)+pow(i[1],2)),1/2)
            if distance <= ks:
                l2.append(i)
        
        return l2
