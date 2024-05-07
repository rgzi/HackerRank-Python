def reverse_words_order_and_swap_cases(sentence):
    reverse_word = list()
    
    for word in sentence:
        if word.isupper():
            word = word.lower() 
            reverse_word.append(word)
        else:
            word = word.upper()
            reverse_word.append(word)  

    reverse_word = "".join(reverse_word)
    reverse_word = reverse_word.split(" ")
    reverse_word = reverse_word[::-1]
    for word in reverse_word:
        print(word, end=" ")
reverse_words_order_and_swap_cases("aWESOME is cODING")
