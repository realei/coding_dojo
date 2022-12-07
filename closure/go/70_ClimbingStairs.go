// Solution - closure
func methodsNum() func() int {
    pre1, pre2 := 1, 1

    return func() int {
        temp := pre1
        pre1, pre2 = pre2, (pre1 + pre2)
        return temp
    }
}

func climbStairs(n int) int {
    f := methodsNum()
    for i := 0; i < n; i++ {
        f()
    }

    return f()
}
