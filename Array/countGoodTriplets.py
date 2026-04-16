class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        x = 0
        for i in range(len(arr)):
           for j in range(1,len(arr)):
            for k in range(2,len(arr)):
                if (0 <= i < j < k < len(arr)) and (abs(arr[i] - arr[j]) <= a) and (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
                    x += 1
        return x





        
