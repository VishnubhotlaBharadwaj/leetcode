class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x > 0:
            s = x%10
            r = r*10 + s
            x = x/10
            if r > (2**31 - 1):
                return 0
        return r* sign
            