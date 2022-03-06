from typing import List
import collections
import sys
import re

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        possible_earns = set()
        nums_set = set(nums)
        for n in nums_set:
            earn = n
            temp_nums = nums.copy()
            temp_nums.remove(n)
            temp_nums = [x for x in temp_nums if x != n-1 and x != n+1]
            earn += self.deleteAndEarn(temp_nums)
            possible_earns.add(earn)
        return max(possible_earns)

if __name__ == '__main__':
    file = open(sys.argv[1])
    lines = file.read().splitlines()
    sol = Solution()
    for line in lines:
        str_lst = re.split(',| ', line)
        lst = [int(i) for i in str_lst]
        print(f"\ntest array: {lst}")
        print(sol.deleteAndEarn(lst))
