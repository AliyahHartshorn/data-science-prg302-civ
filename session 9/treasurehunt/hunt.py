def find_next_file(file_name):
    with open(file_name,"r") as file:
        file_data=file.read()
        print(file_data)
        
        ext_index=file_data.find(".txt")
        if ext_index<0:
            return None
        file_index=file_data.rfind(" ",0,ext_index)
        filename=file_data[file_index+1:ext_index+4]
        return filename

path_prefix="session 9\\treasurehunt\\"
file_name="clue1.txt"
while file_name is not None:
    file_name=find_next_file(path_prefix+file_name)
