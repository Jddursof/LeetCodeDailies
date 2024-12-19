class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        triangles=[((n**2)+n)/(2) for n in range(1,len(arr)+1)]
        val=0
        base=0
        splits=0
        for i,num in enumerate(arr):
            val+=num+1
            #print(val,triangles[i],base,splits)
            if val==(triangles[i]-base):
                #val=0
                splits+=1
                #base=triangles[i]
        #They had a few easy days in a row so I didn't bother. Key insight here was they always had the numbers 0-n-1 in order for a parition to be concatenatable it needs to sum to the triangle number. I think the minus base is unnecessary. It is. 
        return splits
            

        