#Simple file reading example

#The path below will probably be wrong. Right click the "text.txt" file
#in your VS Code explorer and copy relative path. Paste and escape any backslashes.
file = open("session 7\\text.txt","r")
quicktext = file.read()
print(quicktext)
lines=quicktext.split('\n')
print(lines)
