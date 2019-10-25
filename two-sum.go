func twoSum(nums []int, target int) []int {
    res := make([]int, 2)
    
    for k1, v1 := range nums {
        flag := 0
        for k2, v2 := range nums[k1 + 1:] {
            if v1 + v2 == target {
                res[0] = k1
                res[1] = k2 + k1 + 1
                flag = 1
                break
            }
        }
        if flag == 1 {
            break
        }
    }
    
    return res
}
