import doctest


def reverse_words(text):
    """
    >>> reverse_words("abcd")
    'dcba'
    >>> reverse_words("abcd efgh")
    'dcba hgfe'
    >>> reverse_words("")
    ''
    >>> reverse_words("a1bcd efg!h")
    'd1cba hgf!e'
    >>> reverse_words("12345")
    '12345'
    >>> reverse_words(12345)
    Traceback (most recent call last):
        ...
    TypeError: Аргумент повинен бути рядком
    """
    if not isinstance(text, str):
        raise TypeError("Аргумент повинен бути рядком")

    words = text.split(' ')
    result = []

    for word in words:
        letters = []
        for ch in word:
            if ch.isalpha():
                letters.append(ch)

        letters.reverse()

        new_word = ''
        index = 0
        for ch in word:
            if ch.isalpha():
                new_word = new_word + letters[index]
                index = index + 1
            else:
                new_word = new_word + ch

        result.append(new_word)

    final_text = ' '.join(result)
    return final_text


if __name__ == "__main__":
    doctest.testmod(verbose=True)

    text = input("Введіть текст: ")
    print(reverse_words(text))
