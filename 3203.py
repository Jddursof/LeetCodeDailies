def flyod_marshal(edges1: List[List[int]]) -> int:
        n=len(edges1)
        dist1=[[10000000 for i in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            dist1[i][i]=0
        for i in range(n):      
            dist1[edges1[i][0]][edges1[i][1]]=1
            dist1[edges1[i][1]][edges1[i][0]]=1
        for k in range(0,n+1):
            for i in range(0,n+1):
                for j in range(0,n+1):
                    dist1[i][j] = min(dist1[i][j], dist1[i][k]+dist1[k][j])
        mini=1000000
        max_internal=0
        for i in range(len(dist1)):
            mini=min(max(dist1[i]),mini)
            max_internal=max(max(dist1[i]),max_internal)
        return mini,max_internal
class Solution:
               
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        min1,max1=flyod_marshal(edges1)
        min2,max2=flyod_marshal(edges2)

        return max(max(min1+min2+1,max1),max2)
        #Using the floyd marshal should get it in V3. Doesn't pass timeout. A breadth first solution should be able to get it since there are no cycles. I've looked and the answer says to run it twice, once from any node and then once from the farthest node to get the diameter internally.   