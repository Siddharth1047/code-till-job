"""
Given two integer array A and B of size N each.
A sum combination is made by adding one element from array A and another element of array B.
Return the maximum K valid sum combinations from all the possible sum combinations.
Note : Output array must be sorted in non-increasing order.

Example 1:
Input:
N = 2
K = 2
A [ ] = {3, 2}
B [ ] = {1, 4}
Output: {7, 6}
Explanation: 
7 -> (A : 3) + (B : 4)
6 -> (A : 2) + (B : 4)

Example 2:
Input:
N = 4
K = 3
A [ ] = {1, 4, 2, 3}
B [ ] = {2, 5, 1, 6}
Output: {10, 9, 9}
Explanation: 
10 -> (A : 4) + (B : 6)
9 -> (A : 4) + (B : 5)
9 -> (A : 3) + (B : 6)
"""
# Here's my initial attempt

def maxiCombinations(K, A, B):
    arr = []
        
    for i in A:
        for j in B:
            total = i + j
            arr.append(total)
                
    set_arr = set(arr)
    sorted_arr = sorted(list(set_arr), reverse = True)
        
    return sorted_arr[:K]
    
A = [3,2]
B = [1,4]
K = 2
print(maxiCombinations(K, A, B))

# But GFG told me to reduce the time complexity, so after trying multiple times and using ChatGPT
# Here's the accepted result

import heapq

class Solution:
    def maxCombinations(self, N, K, A, B):
        A.sort(reverse = True)
        B.sort(reverse = True)

        max_heap = []
        my_set = set()
        max_sum = A[0] + B[0]

        heapq.heappush(max_heap, (-max_sum, (0, 0)))

        my_set.add((0, 0))
        result = []

        for _ in range(K):
            temp = heapq.heappop(max_heap)
            result.append(-temp[0])
            
            i = temp[1][0]
            j = temp[1][1]
            
            next_sum = []
            
            if (i + 1 < N):
                next_sum.append(A[i + 1] + B[j])
                next_index = (i + 1, j)
                
                if next_index not in my_set:
                    my_set.add(next_index)
                    heapq.heappush(max_heap, (-next_sum[-1], next_index))
                    
            if (i < N) and (j + 1 < N):
                next_sum.append(A[i] + B[j + 1])
                next_index = (i, j + 1)
                
                if next_index not in my_set:
                    my_set.add(next_index)
                    heapq.heappush(max_heap, (-next_sum[-1], next_index))
                    
        return result
    
S = Solution()

N1, K1, A1, B1 = 2, 2, [3, 2], [1, 4]
result1 = S.maxCombinations(N1, K1, A1, B1)
print(result1)  # Output: [7, 6]

N2, K2, A2, B2 = 4, 3, [1, 4, 2, 3], [2, 5, 1, 6]
result2 = S.maxCombinations(N2, K2, A2, B2)
print(result2)  # Output: [10,9,9]