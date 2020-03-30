import re

def encode(text):
    text = text.replace('\n', ' ')
    word_to_number_map = dict()
    words = re.sub(r'[^\s\w]', '', text).split()
    index = 1
    numbers = []
    for word in words:
        if word in word_to_number_map:
            numbers.append(word_to_number_map[word])
        else:
            word_to_number_map[word] = index
            numbers.append(index)
            index += 1

    return word_to_number_map,numbers

t = """
Spain looked to be heading for a seventh straight win in qualification until 
Chelsea goalkeeper Kepa Arrizabalaga brought down Omar Elabdellaoui.
Bournemouth's King rolled home the spot-kick in the 94th minute to leave Norway in 
fourth place in Group F.
Real Madrid's Ramos, 33, made his Spain debut in 2005 and is one of the last survivors of 
a golden era that won a World Cup and two European Championships.
Ramos, who overtook Latvia's Vitalijs Astafjevs at the summit of Europe's outfield caps 
list, is now eight caps from matching Gianluigi Buffon's overall European record of 176 international appearances.
The defender has some way to go if he wants to break the world record, however, 
with former Egypt midfielder Ahmed Hassan playing 184 times for his country between 1995 and 2012.
"""
print(encode(t))