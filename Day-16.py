# Find vowels and consonants in a string

class VowelFinder:
    def __init__(self):
        self.vowel = set()
        self.consonants = set()

    def find_vowels(self, string):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for letter in string:
            if letter in vowels:
                self.vowel.add(letter)
            else:
                self.consonants.add(letter)

    def getVowels(self):
        print("Vowels are:-")
        return self.vowel
    
    def getConsonants(self):
        print("Consonants are:-")
        return self.consonants
    
vf = VowelFinder()
vf.find_vowels("fwghuagihuiefovarjeiojgjpio")
print(vf.getVowels())     
print(vf.getConsonants()) 

# Linear search
def linearSearch(arr, x):
    for i in arr:
        if arr[i] == x:
            return i # return index position
    return -1

print(linearSearch([1,2,3,4,5],5))