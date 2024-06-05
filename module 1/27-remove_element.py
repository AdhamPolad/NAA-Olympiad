
# Two pointer approach
l, r = 0, len(nums) -
while l<=r:
    if nums[l] == val:
        nums[l], nums[r] = nums[r], nums[l] #swapp
        r-=1
    else:
        l+=1
return l
# Time Complexity: O(n)
# Space Complexity: O(1)


# 2nd solution
k = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k+=1
return k

# Time Complexity: O(n)
# Space Complexity: O(1)

