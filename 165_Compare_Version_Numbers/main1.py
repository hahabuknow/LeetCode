import collections
import sys
import re

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        ver1_len = len(ver1)
        ver2_len = len(ver2)
        len_diff = ver1_len - ver2_len
        if len_diff > 0:
            for i in range(0, len_diff):
                ver2.append(0)
        elif len_diff < 0:
            for i in range(len_diff, 0):
                ver1.append(0)
        for i in range(0, len(ver1)):
            num1 = ver1[i]
            num2 = ver2[i]
            if int(num1) < int(num2):
                return -1
            elif int(num1) > int(num2):
                return 1
            i += 1
        return 0

if __name__ == '__main__':
    file = open(sys.argv[1])
    lines = file.read().splitlines()
    sol = Solution()
    for line in lines:
        str_lst = re.split(',| ', line)
        ver1 = str_lst[0]
        ver2 = str_lst[1]
        print(f"\ntest versions: {ver1} vs {ver2}")
        print(sol.compareVersion(ver1, ver2))
