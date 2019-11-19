from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
import os
# data = "Mars is a cold desert world. It is half the size of Earth. "
# print(sent_tokenize(data))
# 
# data = "Mars is approximately half the diameter of Earth."
# print(word_tokenize(data))

def checkReleventTweet(eventName, tweetContent):
file_docs = []

with open ('demofile.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file_docs.append(line)
        print(line)

print("Number of documents:",len(file_docs))

gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in file_docs]

print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print("Dictionary creation: ", dictionary.token2id)

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print("Bag of Words: ",corpus)

tfidf = gensim.models.TfidfModel(corpus)
# for doc in tfidf[corpus]:
#     print([[mydict[id], np.around(freq, decimals=2)] for id, freq in doc])
    
# building the index
sims = gensim.similarities.Similarity(os.getcwd(),tfidf[corpus],
                                        num_features=len(dictionary))
print(sims)
print(type(sims))

file2_docs = []

with open ('demofile2.txt') as f:
    tokens = sent_tokenize(f.read())
    for line in tokens:
        file2_docs.append(line)

print("Number of documents:",len(file2_docs))  
for line in file2_docs:
    query_doc = [w.lower() for w in word_tokenize(line)]
    query_doc_bow = dictionary.doc2bow(query_doc) #update an existing dictionary and create bag of words

print("Updated Bag of words after reading 2nd file")
# perform a similarity query against the corpus
query_doc_tf_idf = tfidf[query_doc_bow]
print("Updated Bag of words after reading 2nd file")

print("Current path: ",os.getcwd())

print('Comparing Result:', sims[query_doc_tf_idf]) 

import numpy as np

sum_of_sims =(np.sum(sims[query_doc_tf_idf], dtype=np.float32))
print(sum_of_sims)

percentage_of_similarity = round(float((sum_of_sims / len(file_docs)) * 100))
print(f'Average similarity float: {float(sum_of_sims / len(file_docs))}')
#print(f'Average similarity percentage: {float(sum_of_sims / len(file_docs)) * 100}')
print(f'Average similarity rounded percentage: {percentage_of_similarity}')



