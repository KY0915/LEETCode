class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nxt=0
        sum=nums[0]
        for i in range(1,len(nums)):
            sum^=nums[i]
        return sum
'''

2(2,1)-(2,2,1)
6-5
1

2(4,1,2)-(4,1,2,1,2)
14-10
4
'''
