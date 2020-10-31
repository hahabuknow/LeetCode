# 55. Jump Game

Problem: https://leetcode.com/problems/jump-game/

### main.py

Using a map locTag to record the result of num[idx:]

The recursive way makes the efficiency bad and it exceeds time limit on the last test case.

**Last test case:** 

An array with size 25003: [25000,24999,24998, ...,4,3,2,1,1,0,0]


### main1.py

Loop the nums array from left. Only loop once with time complexity `O(n)`.
