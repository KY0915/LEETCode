class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise= nums[0]
        hare = nums[0]
        
        while True:
            tortoise= nums[tortoise]
            hare= nums[nums[hare]]
            
            if hare==tortoise:
                break
                
        ptr1=nums[0]
        ptr2=hare
        
        while ptr1!=ptr2:
            ptr1=nums[ptr1]
            ptr2=nums[ptr2]
            
        return ptr1
