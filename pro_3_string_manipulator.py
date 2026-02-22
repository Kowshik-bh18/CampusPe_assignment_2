# string manipulator program
# this program performs various operations on a sentence

text = input("enter a sentence: ")
words = text.split()

print("original:", text)
print("characters with spaces:", len(text))
print("characters without spaces:", len(text.replace(" ", "")))
print("total words:", len(words))
print("uppercase:", text.upper())
print("lowercase:", text.lower())
print("title case:", text.title())
print("first word:", words[0] if words else "")
print("last word:", words[-1] if words else "")
print("reversed:", text[::-1])
