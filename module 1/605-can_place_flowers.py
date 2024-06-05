class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0

        if n ==0:
            return True
        
        for i in range(length):
            if flowerbed[i] == 0:
                empty_prev = (i==0) or (flowerbed[i-1]==0)
                empty_next = (i==length-1) or (flowerbed[i+1]==0)

                if empty_prev and empty_next:
                    count +=1
                    flowerbed[i] = 1
        return count >= n


# Time Complexity: O(n)
# Space Complexity: O(n)