func rowGenerator() func() [] int {
    row := 1
    preRow := make([]int, row)

    return func() [] int {
        vals := make([]int, row) 
        for i := 0; i < row; i++{
            if i < 2 {
                vals = append(vals, 1)
            } else {
                vals = append(vals, preRow[i] + preRow[i - 1])
            }
        }
        
        preRow := vals
        return vals
    }
}

func getRow(rowIndex int) []int {
    f := rowGenerator()
    for i := 0; i < rowIndex + 1; i++ {
        f()
    }

    return f()
}
