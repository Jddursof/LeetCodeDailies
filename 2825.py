class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        #Make two strings a substring by cyclically shifting characters after a point
        #Initial Thoughts, find the first index where they don't match, do the cypher and then keep checking
        if len(str1)<len(str2):
            return False
        i=0
        j=0
        letters="abcdefghijklmnopqrstuvwxyz"
        shift_dict={letters[i]: letters[(i+1)%26] for i in range(len(letters))}
        while(i<len(str1) and j<len(str2)):
            if str1[i]==str2[j] or shift_dict[str1[i]]==str2[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j==len(str2):
            return True
        else:
            return False
        #Final thoughts, I misunderstood what the substring task was. The actual problem was much easier, simply check if the character in string 2 matches the character in string 1 or the character in string 1 plus the cypher. If it doesn't that letter cannot be a part of the solution. Final time 10 mins
        