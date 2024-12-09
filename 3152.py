class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        break_left=[0]*(len(nums)+1)
        for i in range(1,len(nums)):
            break_left[i]=break_left[i-1]+(nums[i]%2==nums[i-1]%2)
        #print(break_left)
        answer_list=[]
        for query in queries:
            if break_left[query[0]]==break_left[query[1]]:
                answer_list.append(True)
            else:
                answer_list.append(False)
        return answer_list
        #Pretty happy with this one. I knew there was a transformation of the data that would help and eventually I thought of the cumulative number of breaks. 
        