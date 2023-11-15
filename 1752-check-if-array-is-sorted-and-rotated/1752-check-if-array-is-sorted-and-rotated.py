class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range (len(nums)):
            if nums == sorted(nums):
                return True
            nums= nums[1 : ] + [nums[0]]
        return False