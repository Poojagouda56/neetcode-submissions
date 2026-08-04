class Solution:
    # def squareSum(self,n):
    #     total=0
    #     while n:
    #         d=n%10
    #         total+=d*d
    #         n//=10
    #     return total
    # def isHappy(self, n: int) -> bool:
    #     slow=n
    #     fast=self.squareSum(n)
    #     while fast!=1 and slow !=fast:
    #         slow=self.squareSum(slow)
    #         fast=self.squareSum(self.squareSum(fast))
    #     return fast==1
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1 and n not in seen:
            seen.add(n)
            total=0
            while n>0:
                digit=n%10
                total+=digit*digit
                n//=10
            n=total
        return n==1