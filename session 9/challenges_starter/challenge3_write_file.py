# Open the file in read mode
file_path = "sample.txt"
with open(file_path, "r") as file:
    content = file.read()
    lines = content.split('\n')
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)

# Append a new line to the file
new_line = "Thank you for participating in this challenge!"
with open(file_path, "a") as file:
    file.write(new_line + '\n')

# # Overwrite the file with new content
# new_content = "This is the new content of the file."
# with open(file_path, "w") as file:
#     file.write(new_content)

# Print the results
print("Total lines in the file:", total_lines)
print("Total words in the file:", total_words)
