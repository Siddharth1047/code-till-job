"""
Given a directed graph, determine whether a vertex j is reachable from another vertex i for all vertex pairs (i, j) 
in the given graph. Here, vertex j is reachable from another vertex i means that there is a path from vertex i to j. 
The reachability matrix is called the transitive closure of a graph. The directed graph is represented by an adjacency 
matrix where there are N vertices. 

Example 1:
Input: N = 4
graph = {{1, 1, 0, 1}, 
         {0, 1, 1, 0}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
Output: {{1, 1, 1, 1}, 
         {0, 1, 1, 1}, 
         {0, 0, 1, 1}, 
         {0, 0, 0, 1}}
Explanation: 
The output list shows the reachable indexes.

Example 2:
Input: N = 3
graph = {{1, 0, 0}, 
         {0, 1, 0}, 
         {0, 0, 1}
Output: {{1, 0, 0}, 
         {0, 1, 0}, 
         {0, 0, 1}
Explanation: 
The output list shows the reachable indexes.
"""
# GFG - POTD 17-10-2023
class Solution:
    def transitiveClosure(self, N, graph):
        # code here
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if (graph[i][k] and graph[k][j]) or i == j:
                        graph[i][j] = 1
        return graph
    
"""
Given a linked list sorted in ascending order and an integer called data, 
insert data in the linked list such that the list remains sorted.

Example 1:
Input:
LinkedList: 25->36->47->58->69->80
data: 19
Output: 
19 25 36 47 58 69 80
Explanation:
After inserting 19 the sorted linked list will look like the one in the output.

Example 2:
Input:
LinkedList: 50->100
data: 75
Output: 
50 75 100
Explanation:
After inserting 75 the sorted linked list will look like the one in the output.
"""
class Solution:
    def sortedInsert(self, head1,key):
        n=Node(key)
        if head1.next is None or key<head1.data:
             n=Node(key)
             n.next=head1                   
             return n

        temp=head1.next
        curr=head1
       
        while temp:
            if temp.data>key:
                n.next=temp
                curr.next=n
                return head1
                
            curr=temp
            temp=temp.next
               
                
        curr.next=n
        return head1