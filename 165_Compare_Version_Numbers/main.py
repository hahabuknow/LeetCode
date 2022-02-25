import collections
import sys
import re

class Solution:
    def process_version(self, version: str) -> str:
        ver_lst = version.split(".")
        processed_ver_num = []
        zero_prefix_regex = r'^0+([1-9]+\d*|0)'
        for n in ver_lst:
            match = re.match(zero_prefix_regex, n) 
            if match:
                processed_ver_num.append(match.group(1))
            else:
                processed_ver_num.append(n)
        processed_ver_str = '.'.join(processed_ver_num)
        zero_tail_regex = r'(.*[1-9]+\d*)(.0)+$'
        zero_tail_match = re.match(zero_tail_regex, processed_ver_str)
        if zero_tail_match:
            processed_ver_str = zero_tail_match.group(1)
        return processed_ver_str

    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = self.process_version(version1).split(".")
        ver2 = self.process_version(version2).split(".")
        print(f"processed: {ver1} vs {ver2}")
        i = 0
        while (i < len(ver1) and i < len(ver2)):
            num1 = ver1[i]
            num2 = ver2[i]
            if int(num1) < int(num2):
                return -1
            elif int(num1) > int(num2):
                return 1
            i += 1
        if len(ver1) > len(ver2):
            return 1
        elif len(ver1) < len(ver2):
            return -1
        else:
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
