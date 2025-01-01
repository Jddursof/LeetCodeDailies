class Solution:
    def maxScore(self, s: str) -> int:
        cumulative_zs=[0]*len(s)
        cumulative_os=[0]*len(s)
        for i,d in enumerate(s):
            cumulative_zs[i]=cumulative_zs[i-1]+(d=="0")
            cumulative_os[i]=cumulative_os[i-1]+(d=="1")
        for i in range(len(cumulative_os)):
            cumulative_os[i]=cumulative_os[-1]-cumulative_os[i]
        total=0
        for i in range(len(cumulative_os)-1):
            total=max(cumulative_os[i]+cumulative_zs[i],total)
        return total



        