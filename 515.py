# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        #Seems like a classic bfs problem, I guess the only trick is to compute the max as you go rather than storing all the nodes and then computing the max. 
        q=[root]
        answer=[root.val]
        while q:
            curr_max=-sys.maxsize - 1
            temp=q
            q=[]
            for node in temp:
                if node.left:
                    q.append(node.left)
                    curr_max=max(node.left.val,curr_max)
                if node.right:
                    q.append(node.right)
                    curr_max=max(node.right.val,curr_max)
            answer.append(curr_max)
        return answer[:-1]

        