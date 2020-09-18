"""
I give you a string, let me know if this string could form a palindrome.

Examples of palindromes: aba, aaaabaaaa, zabaz.

Input: abcurrbac => TRUE;
Input: lkhfadpdfsjafdskldfsafYYYYYYYYYYYYYYY = FALSE;
Input: abc = FALSE;
Input: APPE = FALSE;

"""


from collections import defaultdict

def couldBePalindromeDictionary(input : str):
    letterCounter = defaultdict(lambda:0)
    for c in input:
        letterCounter[c]+=1
    if len(letterCounter) == 1:
        return True
    odds = 0
    for letter in letterCounter:
        if(letterCounter[letter]%2 != 0):
            odds+=1
            if odds > 1:
                return False
    return True


def couldBePalindromeArray(input: str):
    letterCounter = [0] * 128
    for c in input:
        letterCounter[ord(c)-97]+=1
    odds = 0
    for c in letterCounter:
        if(c == 0):
            continue
        elif(c % 2 != 0):
            odds+=1
            if odds > 1:
                return False
    return True



test_cases = ["abcdd", "abccbai", "abcabcdddd", "abcabcddddi", "hkdhakhdajkhdaw", "abcurrbac", "lkhfadpdfsjafdskldfsafYYYYYYYYYYYYYYY", "abc", "APPE", "aaaaa", "abcdddddjjjjjabc", "aaaaabbbbb", "aaaabbbbb", "aaabb", "$$$$$$AA", "aA", "/&(888)"]
for case in test_cases:
    print("------------------------")
    print("Dictionary - Input:", case, couldBePalindromeDictionary(case))
    print("Array - Input:", case, couldBePalindromeArray(case))
    
num = 38
print(1 + (num-1) % 9)