from typing import List
from collections import Counter
import sys
import re

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        lucky = -1
        for k, v in cnt.items():
            if k == v and k > lucky:
                lucky = k
        return lucky

if __name__ == '__main__':
    file = open(sys.argv[1])
    lines = file.read().splitlines()
    sol = Solution()
    for line in lines:
        str_lst = re.split(',| ', line)
        lst = [int(i) for i in str_lst]
        print(f"\ntest array: {lst}")
        print(sol.findLucky(lst))
