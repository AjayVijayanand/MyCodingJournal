def isPalindrome(word):
    if len(word) > 1:
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else:
            return False
    else:
        return True

word = "racecars"
print(isPalindrome(word))