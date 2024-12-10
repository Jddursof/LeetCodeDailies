class Solution:
    def maximumLength(self, s: str) -> int:
        #Longest substring that occurrs thrice composed entirely of one letter
        #This one just seems to be about storage
        special_dict={l: [] for l in "Aabcdefghjiklmnopqrstuvwxyz"}
        last_character="A"
        count=0
        for i,l in enumerate(s):
            if l==last_character:
                count+=1
                continue
            else:
                special_dict[last_character].append(count)
                last_character=l
                count=1
        #To finish
        special_dict[last_character].append(count)
        max_len=-1
        for letter in "abcdefghijklmnopqrstuvwxyz":
            candidate=-1
            if sum(special_dict[letter])>=3:
                temp_list=special_dict[letter]
                temp_list.sort()
                if len(temp_list)==1:
                    candidate=temp_list[0]-2
                elif len(temp_list)==2:
                    c1=temp_list[1]-2
                    c2=min(temp_list[1]-1,temp_list[0])
                    candidate=max(c1,c2)
                elif len(temp_list)>2:
                    c1=temp_list[-1]-2
                    c2=min(temp_list[-1]-1,temp_list[-2])
                    c3=min(min(temp_list[-1],temp_list[-2]),temp_list[-3])
                    candidate=max(max(c1,c2),c3)
            max_len=max(candidate,max_len)
        #Longer than I thought, with a lot of extra memory but methodical. High speed solution. Apparently binary search solution was faster. This should be O(N) so long as I only keep the top three elements in the array so for large arrays that would be a good optimization. 
        return max_len


            

        