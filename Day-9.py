# Roman to Integer (LeetCode).

class Solution:
    def romanToint(self, s: str) -> int:
        # dictionary
        rti = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0

        for i in range(len(s) - 1):
            if rti[s[i]] < rti[s[i + 1]]:
                ans = ans - rti[s[i]]
            else:
                ans  = ans + rti[s[i]]

        return ans + rti[s[-1]]
    
# Test case
s = Solution()
roman_numeral = "MCMXCIV"
integer_value = s.romanToint(roman_numeral)
print("Roman Numeral:", roman_numeral)
print("Integer Value:", integer_value)

# Test case 2
roman_num = "MDCCCLXXVI"
integer_val = s.romanToint(roman_num)
print("Roman Numeral:", roman_num)
print("Integer Value:", integer_val)

# Remove an element from the array and print that number along with the array

def removedElements(arr, n):

    for i in arr:
        if arr[i] == n:
            arr.remove(n)
        
    return arr, n
    
print(removedElements([1,2,3,4,3,4], 4))

