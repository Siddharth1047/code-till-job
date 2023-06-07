"""
Both problems are on LeetCode.
Climbing Stairs: - 
You're climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example: -
Input: n = 3
Output: 3
Explanation: - 
1. 1 + 1 + 1
2. 1 + 2
3. 2 + 1
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one
    
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])
    
s = Solution()
result = s.climbStairs(5)
print("Solution to 1st problem is: ", result)

result2 = s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print("Solution to 2nd problem is: ",result2)

"""
Min Cost Climbing Stairs: -
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
------------------------------------------------------------------------------------------------
Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

