class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        #Easily Done with n*2k time, is there better? Lets see
        if 0: 
            #This solution was too slow
            #Changing range_dict to range_arr 
            #Array was faster but doesn't quite cut it
            curr_best=1
            range_dict=[0]*(10**5+1)
            for num in nums:
                for j in range(max(num-k,0),min(num+k+1,10**5)):
                    range_dict[j]+=1
                    if range_dict[j]>curr_best:
                        curr_best=range_dict[j]
        if 1:
            #turn each num into a range
            range_arr=[]
            for num in nums:
                range_arr.append((num - k, 1))
                range_arr.append((num + k+1, -1))
            range_arr.sort()
            max_val=0
            curr_val=0
            for value,effect in range_arr:
                curr_val+=effect
                max_val=max(max_val,curr_val)
            #Kind of like a custom cumsum like yesterday
        return max_val

        