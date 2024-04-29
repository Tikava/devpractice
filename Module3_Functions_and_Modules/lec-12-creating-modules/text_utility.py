def total_words_count(text): #Выводит сколько всего слов в тексте.
    words = text.split(' ')
    return len(words)

def word_count(word, text): #Выводит сколько раз слово/символ встречается в тексте.
    count = 0
    for w in text.split(' '):
        if word in w:
            count += 1
    return count