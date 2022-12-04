class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        def row_generator(row: int) -> List[int]:
            vals = []
            for i in range(0, row + 1):
                if i == 0 or i == row:
                    vals.append(1)
                else:
                    vals.append(ret[row - 1][i] + ret[row - 1][i - 1])
                    
            return vals

        for row in range(numRows):
            ret.append(row_generator(row))

        return ret 
