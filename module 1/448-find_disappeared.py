class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = {}
        result = []

        for i in range(1, n+1):
            a[i] = 0 
        
        for i in nums:
            a[i] += 1
        
        for key, value in a.items():
            if value == 0:
                result.append(key)

        return result

# Time Complexity: O(n)
# Space Complexity: O(n)


#or

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) -1
            if nums[index]>0:
                nums[index] = -nums[index]
                
        return [i+1 for i in range(len(nums)) if nums[i]>0]
        

# Time complexity: O(n)
# Space complexity: O(1)