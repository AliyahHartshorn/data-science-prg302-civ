def find_next_file(file_name):
    return None

path_prefix=""
file_name=input("Where to start? ")
while file_name is not None:
    file_name=find_next_file(path_prefix+file_name)
