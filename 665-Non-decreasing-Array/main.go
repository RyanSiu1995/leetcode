package leetcode_665

func checkPossibility(nums []int) bool {
    possible := true
    for i := 0; i < len(nums) - 1; i++ {
        elem := nums[i]
        if ! (elem <= nums[i+1]) {
            if !possible {
                return false
            } else {
                possible = false
                if i < len(nums)-2 && nums[i+2] < nums[i] {
                    if i != 0 && nums[i-1] > nums[i+1] {
                        return false
                    }
                    nums[i] = nums[i+2]
                } else {
                    nums[i+1] = nums[i]
                }
            }
        }
    }
    return true
}
