from typing import List
import collections
import sys
import re

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_rec = {}
        for num in arr:
            if num in lucky_rec:
                lucky_rec[num] += 1
            else:
                lucky_rec[num] = 1
                
        od = collections.OrderedDict(reversed(sorted(lucky_rec.items())))
        for k, v in od.items():
            if k == v:
                return k
        return -1

if __name__ == '__main__':
    file = open(sys.argv[1])
    lines = file.read().splitlines()
    sol = Solution()
    for line in lines:
        str_lst = re.split(',| ', line)
        lst = [int(i) for i in str_lst]
        print(f"\ntest array: {lst}")
        print(sol.findLucky(lst))
