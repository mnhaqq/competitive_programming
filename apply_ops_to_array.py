class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def move_zeroes(nums):
            p1 = p2 = 0

            while p1 < len(nums):
                if nums[p1] == 0:
                    p1 += 1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1+=1
                    p2+=1

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1] = 0
        move_zeroes(nums)
        return nums