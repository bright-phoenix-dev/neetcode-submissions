class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for i in s:
            if i.isalnum():
                word+=i.lower()
        print(word)
        return word==word[::-1]
           