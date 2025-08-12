def filter_a_words(word_list):
  """
  Filters a list of strings, removing any word that starts with the letter 'a'.

  This function is case-insensitive, meaning it will remove words starting
  with either 'a' or 'A'.

  Args:
    word_list: A list of strings.

  Returns:
    A new list containing only the words that do not start with 'a'.
  """
  filtered_list = []
  for word in word_list:
    # We use .lower() to make the check case-insensitive.
    # The startswith() method checks if the string begins with the specified prefix.
    if not word.lower().startswith('a'):
      filtered_list.append(word)
  return filtered_list

# --- Example Usage ---

# A sample list of words
sample_words = ["Apple", "Banana", "Ant", "Cherry", "apricot", "Date", "avocado"]

# Call the function with the sample list
filtered_words = filter_a_words(sample_words)

# Print the original and filtered lists to see the result
print(f"Original list: {sample_words}")
print(f"Filtered list: {filtered_words}")

# --- Alternative using List Comprehension (more concise) ---

def filter_a_words_comprehension(word_list):
  """
  Filters a list of strings using a list comprehension.

  This provides a more compact way to achieve the same result.

  Args:
    word_list: A list of strings.

  Returns:
    A new list containing only the words that do not start with 'a'.
  """
  return [word for word in word_list if not word.lower().startswith('a')]

# Example usage for the comprehension version
filtered_comp = filter_a_words_comprehension(sample_words)
print("\n--- Using List Comprehension ---")
print(f"Original list: {sample_words}")
print(f"Filtered list: {filtered_comp}")
