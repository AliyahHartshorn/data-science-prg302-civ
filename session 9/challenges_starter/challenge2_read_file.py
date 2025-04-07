# Open the file in read mode
file=open("session 9\\challenges_starter\\sample.txt","r")
file_data=file.readlines()
file.close()

def remove_whitespace(string_val):
    return string_val.strip()

for item in file_data:
    print(item)
file_data=map(lambda x:x.strip(),file_data)
file_data=map(remove_whitespace,file_data)
for item in file_data:
    print(item)
    # Create variables for the count

    # Loop through each line in the file
        # Split the line into a list of words and count them
    # Print the results
