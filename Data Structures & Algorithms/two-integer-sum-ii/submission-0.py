class Solution:
    def twoSum(self, n: List[int], target: int) -> List[int]:
        res=[0,0]
        i=0
        j=len(n)-1
        while(i<j):
            if n[i]+n[j]==target:
                res[0]=i+1
                res[1]=j+1
                break
            elif n[i]+n[j]>target:
                j-=1
            else:
                i+=1
        return res