import preprocessutils
import re

tokenize_method = preprocessutils.tokenize_SpaCy
query = "-alice +loves +the sun^3"
query = " " + query + " "
# print(query)

pos = re.findall("\+(.*?)\s+",query)
pos = [tokenize_method(q)[0] for q in pos if len(tokenize_method(q)) > 0]
# print(pos)


neg = re.findall("\-(.*?)\s+",query)
neg = [tokenize_method(q)[0] for q in neg if len(tokenize_method(q)) > 0]
# print(neg)

mult = re.findall("(?<=\s)([A-Za-z]+\^[0-9]+)", query)
# print(mult) #includes exponent number

m = {}
for t in mult:
    # print(t)
    exp = re.findall("[0-9]+", t)[0]
    word = tokenize_method(re.findall("[A-Za-z]+", t)[0])
    if len(word) > 0:
        word = word[0] 
        if word in m.keys():
            if int(exp) > m[word]:
                m[word] = int(exp)
        else:
            m[word] = int(exp)

# print(m)
mult_words = list(m.keys())
# print(mult_words)
# print(query)
#remove all +, -, \^[0-9]+ before tokenizing entire query
query = query.replace("+", "")
# print(query)
query = query.replace("-", "")
# print(query)
for word in mult:
    exp = re.findall("\^[0-9]+", word)
    query = query.replace(exp[0], "")
query = query.strip()
# print(query)
all_tokens = tokenize_method(query)
# print(all_tokens)