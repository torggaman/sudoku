def ispalindrome():
    word = input("What word do you want to check?")
    word2 = word.lower()
    if word2 == word2[::-1]:
        return True
    else:
        print(word2)
        print(word2[::-1])
        return False

print(ispalindrome())
