import random

print('''
  __  __             _      ___  ____        _ _ 
 |  \/  |           (_)    / _ \|  _ \      | | |
 | \  / | __ _  __ _ _  __| (_) | |_) | __ _| | |
 | |\/| |/ _` |/ _` | |/ __> _ <|  _ < / _` | | |
 | |  | | (_| | (_| | | (_| (_) | |_) | (_| | | |
 |_|  |_|\__,_|\__, |_|\___\___/|____/ \__,_|_|_|
                __/ |                            
               |___/                             
''')
print('''
        ____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """"........
''')
print("<------------------------------->")

question_asked = input("Ask your question: ")

phrase_list = ['Nah, not likely',
               'No, I doubt that will ever happen',
               'Yeah, probably',
               'I wouldnt get my hopes up',
               'Definitly',
               'I think its possible',
               'Maybe']

if question_asked == "Is max the greatest programmer ever?":
    print("Yes, He is. There is no one better.")
else:
    print(random.choice(phrase_list))

# Built out of boredom, I'll do more later on.
# Max Kanoe. December 16, 2025
