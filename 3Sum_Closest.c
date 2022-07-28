int cmp(const void *a, const void *b){
    return *(int *)a - *(int *)b;    
}

int threeSumClosest(int* nums, int numsSize, int target){
    if(numsSize<=2)
        return 0;
    qsort(nums, numsSize, sizeof(int), cmp);
    
    int min = nums[0] + nums[1] + nums[2];
    for(int i=0;i<numsSize-2;i++){
        int l=i+1, r=numsSize-1, sum=0;
        while(l<numsSize && l<r){
            sum = nums[l] + nums[r] + nums[i];

            if(sum==target)
              return sum;  
            if(abs(sum-target) < abs(min-target))
                min = sum;
            
            if(sum<target)
                l++;
            else
                r--;
        }
    }//for i
    return min;
}
