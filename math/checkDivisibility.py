class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        product_sum = 1
        temp = n
        while temp > 0:
            last = temp % 10
            digit_sum += last
            product_sum *= last
            temp //= 10
        return n % (digit_sum + product_sum) == 0

        
