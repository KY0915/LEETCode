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
            #Find boundary of the height which is shorter height of the two
            currLeftHeight=height[l]
            currRightHeight=height[r]
            if currLeftHeight < currRightHeight:
                minHeight=height[l]
            else:
                minHeight=height[r]
                
            
          
            #Calculate the area and check if current area is bigger than max area.
            currWater=(r-l) * minHeight
            if maxWater < currWater:
                maxWater=currWater

                
            #Check if left heigth is bigger than right and move the pointer on the opposite side one step.
            if currLeftHeight<currRightHeight:
                counter=0
                tempL=height[l]
                nextL=height[l]
                #if next left height is smaller or equal to current height, skip until its bigger. next left height must also has to be bigger than curr height by 1 so add counter.
                while nextL <=tempL:
                    if l > r:
                        return maxWater
                    l+=1
                    counter+=1
                    nextL=height[l]+counter
            else:
                
                rCounter=0                 
                tempR=height[r]
                nextR=height[r]
                #if next right height is smaller or equal to current right height, skip until its bigger.                
                while nextR <=tempR:
                    if l > r:
                        return maxWater                    
                    r-=1
                    rCounter+=1
                    nextR=height[r]+rCounter
 
        return maxWater
            
                
                
                
