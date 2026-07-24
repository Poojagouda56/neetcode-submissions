class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        ans=[]
        for i in range(len(nums)):
            x=target-nums[i]
            if (x in dict):
                ans.append(dict.get(x))
                ans.append(i)
                return ans
            dict[nums[i]]=i