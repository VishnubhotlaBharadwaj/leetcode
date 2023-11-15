class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        if len(s) == 0:
            return 0
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        else:
            sign = 1
        integers = []
        for items in s:
            if items.isdigit():
                integers.append(items)
            else:
                break
        if len(integers) == 0:
            return 0
        else:
            num = int(''.join(integers))
            num *= sign
        num = max(num, -2**31)
        num = min(num, 2**31 - 1)
        return num