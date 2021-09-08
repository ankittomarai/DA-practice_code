class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #return nums + nums
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums
        
        
        # we need to concat two arrays
        # we can run it two times and append
        