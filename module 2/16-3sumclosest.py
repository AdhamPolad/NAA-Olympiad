class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float("inf")
        n = len(nums)
        nums.sort()

        for i in range(n-2):
            j = i+1
            k = n-1

            while j<k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(temp-target) < abs(closest_sum-target):
                    closest_sum = temp
                
                if temp < target:
                    j+=1
                elif temp > target:
                    k-=1
                else:
                    return temp
                    j+=1
                    
        return closest_sum

# Time Complexity: O(nlog(n))
# Space Complexity: O(1)

