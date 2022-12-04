func fibonacci() func() int {
	fib1, fib2 := 0, 1
	
	return func() int {
		temp := fib1
		fib1, fib2 = fib2, (fib1 + fib2)
		return temp
	}

}

func fib(n int) int {
    f := fibonacci()
    for i := 0; i < n; i++ {
        f()
    }

    return f()
}
