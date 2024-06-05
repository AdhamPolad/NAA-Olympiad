class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = {}

        for i in nums:
            a[i] = a.get(i,0) + 1

        for key, value in a.items():
            if value == 1:
                return key


#Time complexity: O(n)
#Space complexity: O(n)