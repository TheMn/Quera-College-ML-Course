def normalize(s):
    res = ""
    for c in s:
        if c.isalnum():
            res = res + c
    return res


def encode(text):
    numbers = []
    code = 1
    dict = {}
    word_to_number_map = {}
    for word in text.split():
        word = normalize(word)
        if word != "":
            if word.lower() in dict:
                numbers.append(dict[word.lower()])
            else:
                dict.setdefault(word.lower(), code)
                numbers.append(dict[word.lower()])
                word_to_number_map.setdefault(word, code)
                code += 1
    return word_to_number_map, numbers


text = """
Vestibulum ac diam sit amet
 quam vehicula elementum sed sit 
 amet dui. Vivamus suscipit tortor eget 
 felis porttitor volutpat. Donec rutrum congue leo eget 
 malesuada. Mauris blandit aliquet elit, eget tincidunt nibh pulvinar a. 
 Curabitur aliquet quam id dui posuere blandit. Curabitur arcu erat, accumsan 
 id imperdiet et, porttitor at sem. Vestibulum ac diam sit amet quam vehicula 
 elementum sed sit amet dui. Curabitur arcu erat, accumsan id imperdiet et,
  porttitor at sem. Quisque velit nisi, pretium ut lacinia in, elementum id enim.
   Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Vestibulum 
   ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Donec 
   velit neque, auctor sit amet aliquam vel, ullamcorper sit amet ligula.

Sed porttitor lectus nibh. Vivamus suscipit tortor eget felis porttitor volutpat.
 Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor 
 sit amet, consectetur adipiscing elit. Curabitur aliquet quam id dui posuere blandit. Curabitur
  arcu erat, accumsan id imperdiet et, porttitor at sem. Quisque velit nisi, pretium ut
   lacinia in, elementum id enim. Proin eget tortor risus. Praesent sapien massa, convallis
    a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing 
    elit. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus.
"""

d, numbers = encode(text)
