import sys
from stats import count_words,count_letters,sort

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    args = sys.argv
    if (len(args) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(args[1])
    num = count_words(text)
    print(f"Found {num} total words")
    c = count_letters(text)
    d = sort(c)
    for g in d:
        if g["char"].isalpha():
          print(f"{g["char"]}: {g["num"]}")
    #print(c)

main()
