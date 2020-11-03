class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)    
        r=n-1        
        res=set()
        if n < 3:
        	return res;

        nums.sort()
        
        for i in range(n-2):        
            if i ==  0 or (i > 0 and nums[i] != nums[i-1]):
                l=i+1
                r=n-1                
                while l < r:
                    leftNum=nums[l]
                    rightNum=nums[r]                
                    sum = nums[i]+nums[l]+nums[r]          
                    if sum == 0:                    
                        res.add((nums[i],nums[l],nums[r]))
                        while  l < r and nums[r-1] == nums[r]:
                            r-=1    
                        while  l < r and nums[l] == nums[l+1]:
                            l+=1 
                        l+=1
                        r-=1
                    elif sum < 0:
                        l+=1
                    else:
                        r-=1
                    
                
        return list(res)
            
                    
            
        
        
