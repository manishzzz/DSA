
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        # dp[i] = maximum jumps to reach index i from start (index 0)
        # Initialize with -1 means unreachable
        dp = [-1] * n
        
        # Starting point: 0 jumps to reach index 0
        dp[0] = 0
        
        # For each position i (from left to right)
        for i in range(n):
            # If we can't reach index i, skip it
            if dp[i] == -1:
                continue
                
            # Try jumping from i to all future positions j
            for j in range(i + 1, n):
                # Check if jump is allowed by target rule
                if abs(nums[j] - nums[i]) <= target:
                    # If we found a better way to reach j, update it
                    # Current way to j = dp[i] + 1     
                    # Compare with existing dp[j] and take the maximum
                    dp[j] = max(dp[j], dp[i] + 1)
        
        # Return result for last index (or -1 if unreachable)
        return dp[n - 1]