from typing import Callable


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []

        def row_generator() -> Callable:
            row, pre_row = 0, []
            def func() -> List[int]:
                nonlocal row, pre_row
                vals = []
                for i in range(0, row + 1):
                    if i == 0 or i == row:
                        vals.append(1)
                    else:
                        vals.append(pre_row[i] + pre_row[i - 1])
                pre_row = vals
                row += 1
                return vals

            return func

        f = row_generator()
        for row in range(numRows):
            ret.append(f())

        return ret
