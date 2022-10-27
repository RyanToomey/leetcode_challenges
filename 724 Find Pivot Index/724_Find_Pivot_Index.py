class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftside = 0    
        for i,j in enumerate(nums):
            rightside = total - leftside - j
            if rightside == leftside:
                return i
            leftside += j
        return -1 