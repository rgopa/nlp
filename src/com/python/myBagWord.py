import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

file2_docs = []

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]

with open ('demofile2.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)

print("Number of documents:",len(file2_docs))  
for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc) #update an existing dictionary and create bag of words