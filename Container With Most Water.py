class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxWater=0

        if r==1:
            if height[l] < height[r]:
                minHeight=height[l]
            else:
                minHeight=height[r]
                
            return minHeight
        while(l<r):
            if height[l] < height[r]:
                minHeight=height[l]
            else:
                minHeight=height[r]
                
            currWater=(r-l) * minHeight
            if maxWater < currWater:
                maxWater=currWater
            currLeftHeight=height[l]
            currRightHeight=height[r]

            if currLeftHeight<currRightHeight:     
                tempL=height[l]
                nextL=height[l]
                while nextL <=tempL:
                    if l > r:
                        return maxWater
                    l+=1
                    nextL=height[l]
            else:
                tempR=height[r]
                nextR=height[r]
                while nextR <=tempR:
                    if l > r:
                        return maxWater                    
                    r-=1
                    nextR=height[r]
 
        return maxWater
            
                
                
                
