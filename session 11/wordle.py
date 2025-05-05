import wordlist

all_words=wordlist.WordList('iot\\session10\\all_words.txt','John')
print(all_words.name)
print(all_words.has_word("abaca"))
target_words=wordlist.WordList('iot\\session10\\target_words.txt',"Fred")
print(target_words.name)
print(target_words.has_word("abaca"))

print(all_words.name)
print(all_words.has_word("abaca"))

#print("This is Wordle.")
#words=wordlist.load_word_list('iot\\session10\\all_words.txt')
#print('steep' in words)
#t_words=wordlist.load_word_list('iot\\session10\\target_words.txt')
#print('steep' in t_words)

