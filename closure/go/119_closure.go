// 119. Pascal's Triangle II
func rowGenerator() func() [] int {
    row := 0
    var preRow, curRow []int

    return func() [] int {
        curRow = make([]int, row+1)
        for i := 0; i <= row; i++{
            curRow[0], curRow[i] = 1, 1
            for j := 1; j < i; j++ {
                curRow[j] = preRow[j-1] + preRow[j]
            }
        }

        preRow = make([]int, row+1)
        copy(preRow, curRow)
        row++

        return preRow
    }
}

func getRow(rowIndex int) []int {
    f := rowGenerator()
    for i := 0; i < rowIndex; i++ {
        f()
    }

    return f()
}
