"""
The principal has a problem with repetitions. Every time someone sends the same email twice he becomes angry and starts yelling. 
His assistant filters the mails so that all the unique mails are sent only once, and if someone is sending the same mail again and again, 
he deletes them. Write a program that will see the list of roll numbers of the student and find how many emails are to be deleted.

Sample Input:  6,  [ 1, 3, 3, 4, 3, 3 ]
Sample Output: 3
"""

def countDuplicate(arr):
    c = 0

    for i in set(arr):
        if arr.count(i) > 1:
            c += arr.count(i) - 1
    
    return c

arr = [1,3,3,4,3,3]
print(countDuplicate(arr))

"""
Given a string, return the character that appears the minimum number of times in the string. 
The string will contain only ASCII characters, from the ranges       
 ( “a” “z”, “A” “Z”, 0 9 ), and case matters. If there is a tie in the minimum number of times a character
 appears in the string return the character that appears first in the string.

Sample Input: cdadcda
Sample Output: c
Explanation: C and A both are with minimum frequency. So c is the answer because it comes first with less index.
"""

def minString(string):
    ans = []

    for i in string:
        ans.append(string.count(i))
    
    return string[ans.index(min(ans))]

string = "cddabbefff"
print(minString(string))