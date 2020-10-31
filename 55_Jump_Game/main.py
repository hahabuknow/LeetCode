# this version will result in Time Limit Exceeded.
class Solution:
    def canJump(self, nums):
        self.locTag = {}
        self.oriLen = len(nums)
        self.nums = nums
        return self.canJumpCal(0)

    def canJumpCal(self, idx):
        print("=== check index: " + str(idx) + " ===")
        print(self.locTag)
        if idx in self.locTag:
            print("Found answer for: "+ str(idx))
            return self.locTag[idx]

        step = maxStep = self.nums[idx]
        if maxStep >= len(self.nums[idx:]) - 1:
            self.locTag[idx] = True
            return True
        if maxStep == 0:
            self.locTag[idx] = False
            return False
        while step > 0:
            checkIdx = idx + step
            if self.canJumpCal(checkIdx):
                self.locTag[checkIdx] = True
                return True
            self.locTag[checkIdx] = False
            step -= 1
        return False

if __name__ == '__main__':
    lst = []
    n = int(input("Enter number of elements : ")) 
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    sol = Solution()
    print(sol.canJump(lst))
