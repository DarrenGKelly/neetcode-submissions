class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        totalProduct = 0
        numZeros = 0

        for num in nums:
            if (num != 0):
                if (totalProduct == 0):
                    totalProduct += num
                else:
                    totalProduct *= num
            else:
                numZeros += 1

        for num in nums:
            if (numZeros >= 2):
                products.append(0)
            elif (num != 0):
                if (numZeros == 1):
                    products.append(0)
                else:
                    products.append(int(totalProduct / num))
            else:
                products.append(totalProduct)

        return products