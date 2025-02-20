class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_val = set()
        n = len(nums)
        for num in nums:
            num_val.add(int(num,2))
        ret_val = 0 
        for num in range(n+1):
            if num not in num_val:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans