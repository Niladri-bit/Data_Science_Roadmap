class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}
        for i in range(len(nums)):
            if target-nums[i] in myMap:
                previousIndex = myMap[target-nums[i]]
                return [previousIndex, i]
            myMap[nums[i]] = i
