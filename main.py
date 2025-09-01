from stats import count_words, count_num_chars, sort_counts
import sys

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  book_text = get_book_text(book_path)
  num_words = count_words(book_text)
  letter_counts = count_num_chars(book_text)
  letter_counts_list = sort_counts(letter_counts)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  
  for letter_count in letter_counts_list:
    print(letter_count["char"] + ": " + str(letter_count["num"]))

  print("============= END ===============")

main()