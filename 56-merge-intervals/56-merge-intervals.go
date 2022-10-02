func merge(intervals [][]int) [][]int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] <intervals[j][0] 
    })
    result := make([][]int,0)
    result = append(result, intervals[0])

    for _,nums:=range(intervals[1:]){
        lastNum := result[len(result)-1][1]

        if nums[0]<=lastNum {
            if nums[1] > lastNum{
                result[len(result)-1] = []int{result[len(result)-1][0], nums[1]}
            }
        }else{
            result = append(result, []int{nums[0],nums[1]})}
        }
    return result 
    }