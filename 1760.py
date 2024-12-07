class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        #The goal is to find the largest number in a list of nums after dividing the bag into two new smaller bags
        #My questions is do you actually have to do the operations i.e. search?  
        bags_at_end=len(nums)+maxOperations
        potential_average=math.floor(sum(nums)/bags_at_end)
        high=max(nums)
        low=1
        while low<high:
            mid=(low+high) >> 1
            #print(low,high,mid)
            #How many extra bins we will need
            cnt=sum(math.ceil(x/mid)-1 for x in nums)
            #print(cnt)
            if cnt<=maxOperations:
                high=mid
            else:
                low=mid+1
        return int(high)
        #Need to get used to these, Doing the binary search to see if the binsize works seems like cheating. Also lots of off by 1 errors