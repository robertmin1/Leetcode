func searchInsert(nums []int, target int) int {
    if target > nums[len(nums) -1]{
        return len(nums)
    }
    for key,value:=range(nums){
		if value == target {
			return key
        }else if value>target{
            return key
        }
        }
    return 0
	}
    