class Solution:
    def findScore(self, nums: List[int]) -> int:
        def argsort(seq):
            return sorted(range(len(seq)), key=seq.__getitem__)
        sort_args=argsort(nums)
        marked=[0]*len(sort_args)
        score=0
        total=0
        for i in range(len(sort_args)):
            if not marked[sort_args[i]]:
                marked[sort_args[i]]=1
                if sort_args[i]!=len(sort_args)-1:
                    marked[sort_args[i]+1]=1
                if sort_args[i]!=0:
                    marked[sort_args[i]-1]=1
                score+=nums[sort_args[i]]
                total+=1
            else:
                if total==len(sort_args):
                    return score
                continue
        #I used argsort, apparently a stack and sequential processing gets it in O(n)
        return score




        