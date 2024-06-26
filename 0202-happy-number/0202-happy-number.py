class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashset=set()
        while n!=1:
            n=sum([int(i)**2 for i in str(n)])
            if n in hashset:
                return False
            hashset.add(n)
        return True        