# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        ans = -1
        start = 0
        end = mountain_arr.length() - 1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if mountain_arr.get(mid) > mountain_arr.get(mid+1):
                  end = mid-1
            else:
                start = mid+1
        
        temp = self.binarysearch(target,mountain_arr,start)
        return temp if temp != -1 else self.orderagbinary(target,mountain_arr,start)
                
        
        
        
        
    def binarysearch(self, target: int, mountain_arr: 'MountainArray', peak):
        start = 0
        end = peak
        
        while start <= end:
            mid = start + (end-start)//2
            
            if mountain_arr.get(mid) > target:
                  end = mid-1
            elif mountain_arr.get(mid) < target:
                start = mid+1
            else:
                ans = mid
                return ans 
            
        return -1
    def orderagbinary(self, target: int, mountain_arr: 'MountainArray', peak):
        start = peak+1
        end = mountain_arr.length() - 1
        
        while start <= end:
            mid = start + (end-start)//2
            
            if mountain_arr.get(mid) > target:
                    start = mid+1
            elif mountain_arr.get(mid) < target:
                end = mid-1
            else:
                ans = mid
                return ans 
            
        return -1
        
        
        
        