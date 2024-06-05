class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = []

        for i in nums1:
            if i in nums2 :
                a.append(i)
        
        b = []
        for i in a:
            if i not in b:
                b.append(i) 
        
        return b

#Time Complexity: O(n * m) + O(n^2)
#Space Complexity: O(n)


#or


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

#Time Complexity: O(n + m)
# Space Complexity: O(n + m)
