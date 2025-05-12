import sys
from stats import book_length
from stats import book_chars
from stats import sort_dict


def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents
      
def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
  book_text = get_book_text(sys.argv[1]) 
  word_count = book_length(book_text)
  chars = book_chars(book_text)
  #print(chars)
  sorted_chars = sort_dict(chars)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char_info in sorted_chars:
    char = char_info["char"]
    count = char_info["num"]
    if char.isalpha():
      print(f"{char}: {count}")
  print("============= END ===============")
main()

