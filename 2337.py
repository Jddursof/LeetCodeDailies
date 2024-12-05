class Solution:
    def canChange(self, start: str, target: str) -> bool:
        #Initial thoughts: Two indicies two make sure they match then reset indicies. Things can never jump so if there is an R in the start string and we need an L it will never work.
        i,j=0,0
        start+="D"
        target+="D"
        if len(start)!=len(target):
            return False
        n=len(start)
        while (i<n or j<n):
            #Find the next interesting point
            while i<n and start[i]=='_':
                i+=1
            while j<n and target[j]=='_':
                j+=1
            if start[i]!=target[j]:
                return False #parity is wrong
            elif start[i]=="L" and i<j:
                #index of the left is on the left of where it needs to be
                return False
            elif start[i]=="R" and i>j:
                #index of the right is on the right of where it needs to be
                return False
            i+=1
            j+=1
        return True