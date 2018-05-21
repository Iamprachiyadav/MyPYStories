from nltk.tokenize import sent_tokenize, word_tokenize
example_text = "Well, Miss Brown, it's an imperfect world but it's the only one we got. I guarantee you the day weapons are no longer needed to keep the peace, I'll start making bricks and beams for baby hospitals. "
print( "\n"+ example_text + "\n")
print("\n Sentence Tokenizer :::::: \n\n")
print( sent_tokenize(example_text))
print("\n Word Tokenizer ::::::\n\n")
for i in word_tokenize(example_text):
    print (i)
    
