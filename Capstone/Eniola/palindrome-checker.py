def is_palindrome(s):
    clean_text = ''

    for char in s:
        if char.isalnum():
            clean_text += char.lower()

    reversed_text = clean_text[::-1]

    return clean_text == reversed_text
    
# print(is_palindrome("madam"))
# print(is_palindrome('teeth'))
# print(is_palindrome("racecar"))
# print(is_palindrome("A man, a plan, a canal: Panama"))
# print(is_palindrome("hello"))
# print(is_palindrome(""))
# print(is_palindrome("a"))


## BONUS
def is_palindrome2(s):
    left = 0
    right = len(s) - 1

    while left < right:

        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome2("madam"))
print(is_palindrome2('teeth'))
print(is_palindrome2("racecar"))
print(is_palindrome2("A man, a plan, a canal: Panama"))
print(is_palindrome2("hello"))
print(is_palindrome2(""))
print(is_palindrome2("a"))