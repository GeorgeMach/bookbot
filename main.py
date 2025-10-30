from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath: str) -> str:
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    try:
        text = get_book_text(path)
    except FileNotFoundError:
        print(f"Error: File not found: {path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Could not read {path}: {e}")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    word_count = count_words(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    chars = count_characters(text)
    sorted_chars = sort_characters(chars)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
