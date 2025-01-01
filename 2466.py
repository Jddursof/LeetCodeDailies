class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        #Seems like a dynamic programming problem, then I just sum the amount of ways between low and high
        valids=[0]*(high+1)
        valids[zero]+=1
        valids[one]+=1
        coins=[zero,one]
        for n in range(0,len(valids)):
            for coin in coins:
                if (n-coin)>=0:
                    valids[n]=valids[n-coin]+valids[n]
                #print(valids)
        #print(valids)
        return sum(valids[low:(high+1)])%(10**9+7)
        #It was

        