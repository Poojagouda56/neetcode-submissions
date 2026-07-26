class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        h=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    t=[]
                    t.append(nums[i])
                    t.append(nums[j])
                    t.append(nums[k])
                    if t not in h:
                        h.append(t)
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return h