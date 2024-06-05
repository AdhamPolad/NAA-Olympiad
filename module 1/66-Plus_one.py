class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        a = ""
        arr = []

        for i in digits:
            a += str(i)
        
        a = int(a) +1

        for i in str(a):
            arr.append(int(i))
        
        return arr

# Time complexity - O(n)
# Space Complexity - O(n)


# Optimised approach

n = len(digits)

for i in range(n-1, -1, -1):
    digits[i] += 1
    if digits[i] < 10:
        return digits
    digits[i] = 0

return [1] + digits

# Time Complexity: O(n)
#Space Complexity: O(1)