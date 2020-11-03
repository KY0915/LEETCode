# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         n=len(nums)
#         localMax=0
#         globalMax=float("-inf")
#         if n <=1:
#             return nums[0]
#         for i in range(n):
#             localMax=nums[i]+localMax
#             print(localMax)
#             if localMax>globalMax:
#                 globalMax=localMax            
#             if localMax<0:
#                 localMax=0

#         return globalMax
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        localMax=nums[0]
        globalMax=nums[0]
        for i in range(1,n):
            localMax+=nums[i]
            localMax=max(localMax,nums[i])
            globalMax=max(localMax,globalMax)
            
        return globalMax
