# Open the file in read mode
file_path = "sample.txt"
with open(file_path, "r") as file:
    # Create variables for the count
    total_lines = 0
    total_words = 0

    # Loop through each line in the file
    for line in file:
        total_lines += 1

        # Split the line into a list of words and count them
        words = line.split()
        total_words += len(words)

    # Print the results
    print(f"Total lines in the file: {total_lines}")
    print(f"Total words in the file: {total_words}")
