def recursive_step(letter_counts,targets):
    target=copy.copy(targets)
    #print(len(letter_counts),target)
    if target=="":
        return 1
    if len(letter_counts)<len(target):
        return 0
    else: 
        #print("recursion!")
        #print(letter_counts[0][ord(target[0])-97])
        val1=letter_counts[0][ord(target[0])-97]*recursive_step(letter_counts[1:],target[1:])
        val2=recursive_step(letter_counts[1:],target)
        #print(val1,val2)
        return val1+val2
class Solution:


    def numWays(self, words: List[str], target: str) -> int:
        #Seems like an interesting dynamic programming problem
        #My strategy will be: 
        #1: get the counts of letters and indicies of placement (I also want to consider spaces)
        #2: Starting from the end recursively multiply the number of solutions
        #I.e. Case 2 [abba,baab] target="bab"
        # 1 way to get b last, 3 bs second 1 a third after=3, 1 way to get b in place 3 one way for the remainder =4. Base case, size remaining word> array length left
        #return answer mod 10**9+7
        #BFS also looks possible but with word lengths of 100+ the run time will be 26^n
        n=len(words)
        m=len(words[0])
        print(m,len(target))
        if len(words)>5:
            print(ASDF)
        letter_count=[[0 for _ in "abcdefghijklmnoqrstuvwxyz "] for _ in range(m)]
        for word in words:
            for i,letter in enumerate(word):
                letter_count[i][ord(letter)-97]+=1
        #print(letter_count)
        ways=recursive_step(letter_count,target)
        #print(ways)
        return ways%(10**9+7)
        



        