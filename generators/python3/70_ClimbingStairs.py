from typing import Generator


class Solution:
    def generators(self, max: int) -> Generator[int, int, int]:
        p, q, s, n = 1, 1, 1, 0

        while n < max:
            n += 1
            yield s
            p, q = q, s
            s = p + q

    def climbStairs(self, n: int) -> int:

        for num in self.generators(n):
            pass

        return num
