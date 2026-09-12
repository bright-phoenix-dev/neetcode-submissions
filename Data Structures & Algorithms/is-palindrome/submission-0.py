class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for i in s:
            if i.isalnum():
                word+=i.lower()
        print(word)
        if word==word[::-1]:
            return True
        else:
            return False