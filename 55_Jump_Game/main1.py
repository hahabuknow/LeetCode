class Solution:
    def canJump(self, nums):
        leftmost = len(nums) - 1  # last index
        checkIdx = leftmost - 1
        while checkIdx >= 0:
            if checkIdx + nums[checkIdx] >= leftmost:
                leftmost = checkIdx
            checkIdx -= 1
        if leftmost == 0:
            return True

if __name__ == '__main__':
    lst = []
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    sol = Solution()
    print(sol.canJump(lst))
