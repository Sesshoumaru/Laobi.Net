import string
def checkio(text):
    text = text.lower()

    #方法1：完全面向过程
    # letter = ''
    # letter_count = 0
    # for c in text:
    #     if c.isalpha():
    #         count = text.count(c)
    #         if count > letter_count or (count == letter_count and ord(c) < ord(letter)):
    #             letter_count = count
    #             letter = c
    #
    # return letter

    #方法2 列表推导式 + ascii_lowercase + min
    # return min([(-1 * text.count(ch), ch) for ch in string.ascii_lowercase])[1]

    # 方法3 列表推导式 + ascii_lowercase + max
    #return max(string.ascii_lowercase,key = text.count)

    # 方法4 列表推导式 + min
    return min([(-1 * text.count(ch), ch) for ch in text if ch.isalpha()])[1]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")