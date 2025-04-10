# string_analyzer.py

from string_package import reverse_string, capitalize_words, remove_punctuation
from string_package import count_characters, count_words, average_word_length

def main():
    sentence = input("Enter a sentence: ")

    reversed_sentence = reverse_string(sentence)
    capitalized = capitalize_words(sentence)
    clean = remove_punctuation(sentence)

    print("\nReversed Sentence:", reversed_sentence)
    print("Capitalized:", capitalized)
    print("Without Punctuation:", clean)
    print("Character Count:", count_characters(clean))
    print("Word Count:", count_words(clean))
    print("Average Word Length:", average_word_length(clean))

if __name__ == "__main__":
    main()
