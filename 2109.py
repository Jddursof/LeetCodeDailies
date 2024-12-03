class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #Initial thoughts: Seems easy in python, the problem is likely going to be strings
        #chaning length. Add an adjusment term based on the number of spaces added.
        adjustment=0
        #modification storage in new string
        spaces.append(10**6)
        spaces.insert(0,0)
        base=""
        for i in range(len(spaces)-2,-1,-1):
            base=s[spaces[i]:spaces[i+1]]+" "+base
        return base[:-1]
        #Final time 13 mins, Going backwards seemed to help, fairly slow but in the right order of time. Probably a better way to do a list join with a split list. Base casing may also help. 
            

            
        