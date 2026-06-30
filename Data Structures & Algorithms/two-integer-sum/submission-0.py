class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h={} # <num,i>
        i=0
        ans=[]
        for x in nums:
            if target-x in h:
                ans.append(h[target-x])
                ans.append(i)
            else:
                h[x]=i
            i+=1
        return ans

        