def reverse_string(str):
    reversed_str = ''
    for ch in str:
        reversed_str =  ch+reversed_str 
    return reversed_str
word = "Archana"
print(reverse_string(word))

def reverse_sentence_keeping_character_in_position(sentence):
    words = sentence.split() # Split sentence into list of words # ['More', 'Moolya', 'cafe']
    reversed_words= words[::-1]   # ['cafe', 'Moolya', 'More']
    return ' '.join(reversed_words) # Join back to string
    
sentence = "More Moolya Cafe" # Order of words are reversed
print(reverse_sentence_keeping_character_in_position(sentence))

def reverse_entire_sentence(sentence1):
    return sentence1[::-1]
print(reverse_entire_sentence("More Moolya Cafe"))
print(reverse_entire_sentence("Archana"))
    