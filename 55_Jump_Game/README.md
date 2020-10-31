# 55. Jump Game

Problem: https://leetcode.com/problems/jump-game/

---

### main.py

Using a map locTag to record the result of num[idx:]

The recursive way makes the efficiency bad.

---

### main1.py

Loop the nums array from left. Only loop once with time complexity `O(n)`.
