def count_words(text):
  return len(text.split())

def count_num_chars(text):
  counts = {}
  for word in text.split():
    for letter in word:
      letter_lower = letter.lower()
      if letter_lower in counts:
        counts[letter_lower] += 1
      else:
        counts[letter_lower] = 1
  return counts

def sort_on(counts):
  return counts["num"]

def sort_counts(char_counts):
  char_counts_list = []
  for char_count in char_counts:
    char_counts_list.append({
      "char": char_count,
      "num": char_counts[char_count]
    })
  
  char_counts_list.sort(reverse=True, key=sort_on)
  return char_counts_list

  