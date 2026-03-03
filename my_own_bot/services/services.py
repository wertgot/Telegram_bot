import random

def shuffle_word(word: str):
    return ''.join(random.sample(word, len(word)))


def shuffle_text(text: str):
    shuffled_text = ""
    word = ""
    punctuation = '.,!?;:-—()"\'«»{}[]|/=+&^<> '
    for char in text:
        if char in punctuation and word:
            shuffled_text += shuffle_word(word) + char
            word = ""
        else:
            word += char
    if word:
        shuffled_text += shuffle_word(word)
    return shuffled_text