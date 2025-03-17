phone_book=dict()
phone_book["0400001111"]="John"
phone_book["0401891310"]="Masha"
phone_book["0423852370"]="Xi"
phone_book["0428842329"]="Shah"
phone_book["0429542729"]="Jose"
phone_book["0413541279"]="Masha"
print(phone_book.keys())
print(phone_book.values())
for ph_num in phone_book.keys():
    print(ph_num,phone_book[ph_num])