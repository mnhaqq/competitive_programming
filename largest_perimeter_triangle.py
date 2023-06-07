class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #The sum of the length of the two sides of a triangle is greater than the length of the third side.
        nums.sort()
        largest = 0
        for i in range(0, len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2] and nums[i] + nums[i+1] + nums[i+2] > largest:
                largest = nums[i] + nums[i+1] + nums[i+2]
        return largest