class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        #Seems like a two sum problem but we have to make the array, we always want to include the smallest first? Changing Banned for O(1) access time makes it simple
        banned_dict={}
        for element in banned:
            banned_dict[element]=True
        #Dictionary seems slower than array. Could probably mark array then index
        tot=0
        count=0
        for i in range(1,n+1):
            #print(i,tot,count)
            if i not in banned_dict:
                tot+=i
                count+=1
                if tot>maxSum:
                    return count-1
        return count
             
        