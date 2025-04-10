import string

def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def remove_punctuation(s):
    return s.translate(str.maketrans('', '', string.punctuation))

if __name__ == "__main__":
    test = "hello, world!"
    print(reverse_string(test))
    print(capitalize_words(test))
    print(remove_punctuation(test))
