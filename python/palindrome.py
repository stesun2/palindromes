def palindrome(word):
    # Write code here

    word = word.lower()
    pali_word = word[::-1]

    # print('Original:', word)
    # print('Palidrome word: ', pali_word)

    if (word == pali_word):
        return True
    else:
        return False


# print(palindrome('racecar'))
# print(palindrome('Noon'))
# print(palindrome('ciVic'))
# print(palindrome('nice'))
# print(palindrome('bomb'))
# print(palindrome(434))
# print(palindrome(123))