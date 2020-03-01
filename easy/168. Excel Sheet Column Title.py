class Solution:
    def convertToTitle(self, n: int) -> str:
        alpha_num = ""

        while n > 0:
            modVal = n % 26
            if modVal:
                alpha_num += chr(64 + modVal)

            if modVal == 0:
                alpha_num += "Z"

            n = (n // 26-1)

        return alpha_num


sol = Solution()
print(sol.convertToTitle(702))
# print(ord('A'))
