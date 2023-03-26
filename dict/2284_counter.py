from collections import Counter


class Solution:
    def digitCount(self, num: str) -> bool:
        num_cnt = Counter(num)

        for i in range(len(num)):
            if int(num[i]) != num_cnt.get(str(i), 0):
                return False

        return True
