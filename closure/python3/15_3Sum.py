"""
这个题目用闭包写，太臃肿了
"""
from typing import Callable


class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, k = [], 0

        def sulutionsGenerator() -> Callable:
            def func() -> None:
                vals = []
                i, j = k + 1, len(nums) - 1
                while i < j:  # 3. double pointer
                    s = nums[k] + nums[i] + nums[j]
                    if s < 0:
                        i += 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                    elif s > 0:
                        j -= 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
                    else:
                        res.append([nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1

                return None

            return func

        f = sulutionsGenerator()
        for k in range(len(nums) - 2):
            # because of j > i > k, rests are all positive integer
            if nums[k] > 0:
                break
            # skip the same `nums[k]`
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            f()

        return res
