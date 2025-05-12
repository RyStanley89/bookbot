def book_length(book):
  text = book.split()
  count = len(text)
  return count
  
def book_chars(book):
  chars = {}
  for char in book:
    char = char.lower()
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

def sort_dict(chars):
  # Create an empty list to store our new dictionaries
  chars_list = []
  
  # Loop through each key-value pair in the character dictionary
  for char, count in chars.items():
    # Create a new dictionary with the required format
    char_info = {"char": char, "num": count}
    # Add it to our list
    chars_list.append(char_info)
  
  #Now we need to define how to sort this list
  def sort_on(dict_item):
    return dict_item["num"]
  
  chars_list.sort(reverse=True, key=sort_on)
  
  return chars_list
