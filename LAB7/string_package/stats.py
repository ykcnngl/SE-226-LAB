def count_characters(s):
    return len(s)

def count_words(s):
    return len(s.split())

def average_word_length(s):
    words = s.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)

if __name__ == "__main__":
    test = "hello world"
    print(count_characters(test))
    print(count_words(test))
    print(average_word_length(test))
