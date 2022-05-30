class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        prev = 0
        
        for next_ in range(1, len(nums)):
            if nums[prev] != nums[next_]:
                prev += 1
                nums[prev] = nums[next_]
                
        return prev+1
        
