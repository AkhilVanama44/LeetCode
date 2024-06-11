class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        n=len(encoded)
        arr=[0]*(n+1)
        arr[0]=first
        for i in range(1,n+1):
            arr[i]=encoded[i-1]^arr[i-1]
        return arr
        