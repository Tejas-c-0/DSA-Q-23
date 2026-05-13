# 🚀 Day 23 – Find First and Last Position of Element in Sorted Array

## 📌 Problem

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If the target is not found, return:

```python
[-1, -1]
```

You must write an algorithm with `O(log n)` runtime complexity.

### Example

```python
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

---

# 💡 Approach – Modified Binary Search

Instead of stopping after finding the target:

* perform one binary search for the first occurrence
* perform another binary search for the last occurrence

This keeps the solution efficient while handling duplicates correctly.

---

# ⚙️ Python Solution

```python
class Solution:
    def searchRange(self, nums, target):

        def firstPosition():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        def lastPosition():
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        return [firstPosition(), lastPosition()]
```

---

# 🧠 Dry Run

Input:

```python
nums = [5,7,7,8,8,10]
target = 8
```

### First Position Search

| Left | Right | Mid | nums[mid] | Action             |
| ---- | ----- | --- | --------- | ------------------ |
| 0    | 5     | 2   | 7         | Move Right         |
| 3    | 5     | 4   | 8         | Store 4, Move Left |
| 3    | 3     | 3   | 8         | Store 3, Move Left |

First Position = 3

### Last Position Search

| Left | Right | Mid | nums[mid] | Action              |
| ---- | ----- | --- | --------- | ------------------- |
| 0    | 5     | 2   | 7         | Move Right          |
| 3    | 5     | 4   | 8         | Store 4, Move Right |
| 5    | 5     | 5   | 10        | Move Left           |

Last Position = 4

Final Answer:

```python
[3,4]
```

---

# ⏱️ Complexity Analysis

| Complexity       | Value    |
| ---------------- | -------- |
| Time Complexity  | O(log n) |
| Space Complexity | O(1)     |

---

# 🧠 Key Learning

This problem teaches:

* Advanced Binary Search
* Boundary searching
* Handling duplicates efficiently

Binary Search is not just for finding elements — it can also find boundaries and ranges.

---

# ⚠️ Important Insight

When the target is found:

* move left to search first occurrence
* move right to search last occurrence

This is the core trick of the problem.

---

# 🔗 LeetCode

Find First and Last Position of Element in Sorted Array – LeetCode #34

---

# 📈 Progress Log

✅ Day 23 of DSA Journey

