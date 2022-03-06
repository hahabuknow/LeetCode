from typing import List
import collections
import sys
import re

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        pick_earn = [0]*(max_num+1)
        max_earn = [0]*(max_num+1)
        for n in nums:
            pick_earn[n] += n
        for n in range(1, max_num+1):
            if n == 1:
                max_earn[n] = pick_earn[n]
            else:
                max_earn[n] = max(pick_earn[n]+max_earn[n-2],
                                  max_earn[n-1])
        print(f"pick_earn:{pick_earn}")
        print(f"max_earn:{max_earn}")
        return max_earn[max_num]


if __name__ == '__main__':
    file = open(sys.argv[1])
    lines = file.read().splitlines()
    sol = Solution()
    for line in lines:
        str_lst = re.split(',| ', line)
        lst = [int(i) for i in str_lst]
        print(f"\ntest array: {lst}")
        print(sol.deleteAndEarn(lst))
