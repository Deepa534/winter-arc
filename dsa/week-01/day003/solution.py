class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_product = 1
        digit_sum = 0

        for character in str(n):
            digit = int(character)
            digit_product *= digit
            digit_sum += digit

        return digit_product - digit_sum


print(Solution().subtractProductAndSum(234))
