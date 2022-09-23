package main

import (
	"fmt"
	"sort"
)

func findMedianSortedArrays(nums1 []int, nums2 []int)  float64{
    nums1 = append(nums1, nums2...)
	sort.Ints(nums1)
	if len(nums1)%2 == 0 {
		left := 0
		right := len(nums1)-1
		for{
			if left == right-1 {
				break
			}
			left+=1
			right-=1
		}
		b := float64(nums1[left])+float64(nums1[right])
		
		return float64(b/2)
	}else{
		left := 0
		right := len(nums1)-1
		for{
			if left == right {
				break
			}
			left+=1
			right-=1
		}
		return float64(nums1[left])
	}
	
}