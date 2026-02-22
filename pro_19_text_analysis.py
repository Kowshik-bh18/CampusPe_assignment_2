# text analysis functions


# count words
def count_words(text):
    return len(text.split())


# count vowels
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")


# count consonants
def count_consonants(text):
    return sum(1 for c in text.lower() if c.isalpha() and c not in "aeiou")


# reverse text
def reverse_text(text):
    return text[::-1]


# check palindrome
def is_palindrome(text):
    t = text.replace(" ", "").lower()
    return t == t[::-1]


# remove vowels
def remove_vowels(text):
    return "".join(c for c in text if c.lower() not in "aeiou")


# word frequency
def word_frequency(text):
    freq = {}
    for w in text.lower().split():
        freq[w] = freq.get(w, 0) + 1
    return freq


# longest word
def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)


# main analysis function
def analyze_text():

    text = input("enter text: ")

    print("\n=== text analysis ===")
    print("words:", count_words(text))
    print("vowels:", count_vowels(text))
    print("consonants:", count_consonants(text))
    print("reversed:", reverse_text(text))
    print("palindrome:", "yes" if is_palindrome(text) else "no")
    print("without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print("longest word:", lw, f"({len(lw)} letters)")

    print("word frequency:", word_frequency(text))


# run program
analyze_text()