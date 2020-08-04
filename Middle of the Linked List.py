class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count=0
        original=head
        while head.next != None:
            head=head.next
            count+=1
        
        for i in range((count+1)//2):
            original=original.next
            
        return original
            
            
        
