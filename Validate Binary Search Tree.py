# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        s=[root]
        
        while len(s)!=0:
            root=s.pop()
            
            if root.left==None:
                pass
            else:
                #if left node is less than root node
                if root.left.val<root.val:
                    s.append(root.left)
                else:
                    return False
            
            if root.right==None:
                pass
            else:
                if root.right.val > root.val:
                    s.append(root.right)
                else:
                    return False
            
        return True
                    
                
        
