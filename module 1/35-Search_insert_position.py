# Binary search

l,r = 0, len(nums)-1
while l<=r:
    mid = (l+r)//
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        r = mid -1
    else:
        l = mid+1
return l

# Time Complexity: O(log n)
# Space Complexity: O(1)