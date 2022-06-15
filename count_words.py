def count_words(word):
    string=word
    b=string.split(" ")
    print("word",len(b))
    replac=string.replace(" ","")
    print("elemts",len(replac))
count_words("I love learning")
