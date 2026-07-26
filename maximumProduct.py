class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest1 = largest2 = largest3 = -inf
        smallest1 = smallest2 = inf

        for x in nums:
            # Update 3 largest
            if x > largest1:
                largest3 = largest2
                largest2 = largest1
                largest1 = x
            elif x > largest2:
                largest3 = largest2
                largest2 = x
            elif x > largest3:
                largest3 = x

            # Update 2 smallest
            if x < smallest1:
                smallest2 = smallest1
                smallest1 = x
            elif x < smallest2:
                smallest2 = x

        return max(
            largest1 * largest2 * largest3,
            largest1 * smallest1 * smallest2
        )
