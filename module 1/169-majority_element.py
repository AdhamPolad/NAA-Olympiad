class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        a = {}

        for i in nums:
            a[i] = a.get(i,0) + 1
        
        for keys, value in a.items():
            if value> n/2:
                return keys

#Time Complexity: O(n)
#Space Complexity: O(n)
