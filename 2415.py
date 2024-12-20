# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Change the odd levels of a perfect tree, seems like a breadth first search problem with some accumulator checking if its odd or even every time
        solution =[]
        level_nodes=[root]
        depth=0
        while(level_nodes):
            depth+=1
            temp_nodes=level_nodes
            level_nodes=[]
            level_soln=[]
            for node in temp_nodes:
                if node.left:
                    level_nodes.append(node.left)
                    level_soln.append(node.left.val)
                    level_nodes.append(node.right)
                    level_soln.append(node.right.val)

            if depth%2==1:
                level_soln.reverse()
            for node,value in zip(level_nodes,level_soln):
                node.val=value
            #solution.extend(level_soln)
        return root



        