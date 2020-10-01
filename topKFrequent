class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        class Num:
              def __init__(self, key, value):
                self.value = value
                self.key = key
        def heapify(arr,n,i):
            largest=i
            l=2*i+1
            r=2*i+2
            
            if l< n and arr[l].value> arr[i].value:
                largest=l
            if r < n and arr[r].value > arr[largest].value:
                largest=r
                
            if largest!=i:
                arr[i],arr[largest]=arr[largest],arr[i]
                heapify(arr,n,largest)

        def heapSort(arr):
            n=len(arr)            
            for i in range(n//2-1,-1,-1):
                heapify(arr,n,i)
                
            for i in range(n-1,0,-1):
                arr[0],arr[i]=arr[i],arr[0]
                heapify(arr,i,0)                                
            return arr
        
        if len(nums)==k:
            return nums
        
        d={}    
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1        
        return [ i.key for i in heapSort([Num(key,value) for key,value in d.items()])[-k:]]

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        if k == len(nums):
            return nums
        
        count = Counter(nums)   

        return heapq.nlargest(k, count.keys(), key=count.get) 

