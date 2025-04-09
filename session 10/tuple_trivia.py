#1 create trivia tuple
trivia=("Python", 1991, "Guido van Rossum", "tuple")
#2 print it out
print(trivia)
#3 print the first and last elements
print(trivia[0],trivia[-1])
#4 add a couple of elements to the end
#extended_trivia=(trivia[0],trivia[1],trivia[2],trivia[3],'immutable','sequence')
extended_trivia=trivia+('immutable','sequence')
#5 print it out
print(extended_trivia)
#6 assign first 3 elements and print
(language,year,creator,data_type)=trivia
print(language)
print(year)
print(creator)
#7 made quiz tuple
quiz=[
    ("What year was Python created?",1991),
    ("Who created Python?","Guido van Rossum"),
    ("In what year was Python first released?",1991)
    ]
#8 iterate and print
print(quiz)
for question in quiz:
    (query,answer)=question
    print("Question:",query,"\tAnswer:",answer)