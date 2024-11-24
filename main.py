import sys

def main():
    # Check if a book path was provided
    if len(sys.argv) < 2:
        print("Please provide a book path!")
        print("Example: python script.py books/frankenstein.txt")
        return

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    alpha_chars, freq_chars = get_chars_dict(text)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    
    print("\nCharacter Count (Alphabetically):")
    for letter, count in alpha_chars.items():
        print(f"The letter '{letter}' is used {count} times")
        
    print("\nCharacter Count (By Frequency):")
    for letter, count in freq_chars.items():
        print(f"The letter '{letter}' is used {count} times")

    print("\n--- End of report ---")

def get_num_words(text):
    words = text.split()
    return len(words)
    

def get_chars_dict(text):
    chars = {}
    for c in text:
        if c.isalpha():
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    # Two different sorted versions:
    alpha_sorted = dict(sorted(chars.items()))
    freq_sorted = dict(sorted(chars.items(), key=lambda x: x[1], reverse=True))
    return alpha_sorted, freq_sorted



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
