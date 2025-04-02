# # Open the file in read mode
# file_path = "data.txt"
# with open(file_path, "r") as file:
#     content = file.read()
content = "Python is a versatile programming language. It is widely used for web development and data analysis."

# Find the positions of the substring
start_marker = "versatile programming language."
end_marker = "It is widely used for"
start_index = content.find(start_marker)
end_index = content.find(end_marker) + len(end_marker)

# Extract the substring using the found positions
substring = content[start_index:end_index]

# Replace occurrences of a word in the substring
word_to_replace = "is"
replacement_word = "was"
modified_substring = substring.replace(word_to_replace, replacement_word)

# Print the extracted and modified substrings
print("Extracted Substring:")
print(substring)
print("\nModified Substring:")
print(modified_substring)
