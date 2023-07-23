# Count the number of vowels in a string and return it

def count_Vowel(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_V = 0
    count_C = 0

    for i in str:
        if i in vowels:
            count_V += 1
        else:
            count_C += 1

    return count_V, count_C

str = "Everything is awesome"
str_lower = str.lower()
print(count_Vowel(str_lower))