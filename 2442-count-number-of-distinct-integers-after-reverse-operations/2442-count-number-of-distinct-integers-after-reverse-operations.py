class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l= []
        a = set()
        for n in nums:
            l.append(int(str(n)[::-1]))
        a.update(nums)
        a.update(l)
        return len(a)
            