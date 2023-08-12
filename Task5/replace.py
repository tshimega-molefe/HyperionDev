# Initialize a string variable that contains stupid characters
# Use the replace literal to remove the stupid characters in the string variable with spaces
# Make this uppercase
# Fergie Flip it and Reverse it

stupid_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

smart_sentence = stupid_sentence.replace("!", " ")

print(smart_sentence)

upper_sentence = smart_sentence.upper()

print(upper_sentence)

# Fergie Flipt it and Reverse it

sentence_words = upper_sentence.split()

fergie_flip_it_reverse_it = reversed(sentence_words)

reversed_sentence = ' '.join(fergie_flip_it_reverse_it)

print(reversed_sentence)

