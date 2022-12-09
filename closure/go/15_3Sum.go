import (
    "sort"
)


func solutionsGenerator(k *int, nums *[]int, res *[][]int) func(){
    return func() {
        i, j := *k + 1, len(*nums) - 1
        var s int
        for ;i < j; {
            s = (*nums)[*k] + (*nums)[i] + (*nums)[j]
            if s < 0 {
                i++
                for ;i<j && (*nums)[i] == (*nums)[i-1]; {
                    i++
                } 
            } else if s > 0 {
                j--
                for ;i<j && (*nums)[j] == (*nums)[j+1]; {
                    j--
                }
            } else {
                val := []int{(*nums)[*k], (*nums)[i], (*nums)[j]}
                *res = append(*res, val)
                i++
                j--
                for ;i<j && (*nums)[i] == (*nums)[i-1]; {
                    i++
                }
                for ;i<j && (*nums)[j] == (*nums)[j+1]; {
                    j--
                }
            }
        }
        return

    }

}


func threeSum(nums []int) [][]int {
    sort.Ints(nums)
    res, k := make([][] int, 0), 0

    f := solutionsGenerator(&k, &nums, &res)
    for ;k < len(nums) - 2; k++ {
        if nums[k] > 0 { break }
        if k > 0 && nums[k] == nums[k - 1] { continue }
        f()
    }

    return res
}
