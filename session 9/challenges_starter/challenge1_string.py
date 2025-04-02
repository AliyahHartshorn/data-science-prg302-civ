# Open the file in write mode\
path="session 9\\challenges_starter\\numerics2.txt"
with open(path,"a") as file:
    lines=map(lambda x:str(x)+"\n",range(0,10))
    file.writelines(lines)

# Find the positions of the substring

# Extract the substring using the found positions

# Replace occurrences of a word in the substring

# Print the extracted and modified substrings
