# this version will result in Time Limit Exceeded.
class Solution:
    def canJump(self, nums):
        self.locTag = {}
        self.oriLen = len(nums)
        return self.canJumpCal(nums)

    def canJumpCal(self, subNums):
        subNumsLen = len(subNums)
        loc = self.oriLen - subNumsLen
        if loc in self.locTag:
            return self.locTag[loc]

        maxStep = subNums[0]
        if maxStep >= subNumsLen - 1:
            self.locTag[loc] = True
            return True

        step = 1
        achieve = False
        while step <= maxStep:
            if self.canJumpCal(subNums[step:]):
                self.locTag[loc] = True
                return True
            step += 1
        self.locTag[loc] = False
        return False

if __name__ == '__main__':
    lst = []
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    sol = Solution()
    print(sol.canJump(lst))
