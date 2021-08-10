def num_of_words(s):
    num = 0
    for c in s:
        if c == ' ':
            num += 1
    print("number of words in your sentence is: " , num + 1)
    
sentence = input("please enter your sentence: ")
num_of_words(sentence)