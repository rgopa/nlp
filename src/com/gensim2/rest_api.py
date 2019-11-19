from flask import  Flask  #pip3 install Flask
from flask.json import jsonify
from flask import request
from nltk.tokenize import word_tokenize, sent_tokenize
import gensim
import os
app = Flask(__name__)

def checkReleventTweet(eventName, twittText):
    file_docs = []

#     with open ('demofile.txt') as f:
    tokens = sent_tokenize(twittText)
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
    sims = gensim.similarities.Similarity(os.getcwd(),tfidf[corpus],
                                        num_features=len(dictionary))
    print(sims)
    print(type(sims))

    file2_docs = []
    
#     with open ('demofile2.txt') as f:
    tokens = sent_tokenize(eventName)
    for line in tokens:
        file2_docs.append(line)

    print("Number of documents:",len(file2_docs))  
    for line in file2_docs:
        query_doc = [w.lower() for w in word_tokenize(line)]
        query_doc_bow = dictionary.doc2bow(query_doc)
        
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
    
    return percentage_of_similarity
    
@app.route('/createTweet/<eventName>',methods=['POST'])
def createTweet(eventName):
    print('Inside the createTweet method')
    print(request)
    print("EventName: ",eventName)
    twitter_dict = request.get_json()
#     listOfTwittNames = []
    count = 0;
    call = 0;
    for eachTwitt in twitter_dict['tweets']:
        twittText = eachTwitt['full_text']
        call = call+1
        print("call: ",call)
        similarPerc = checkReleventTweet(eventName,twittText)
        if similarPerc > 0:
            count = count+1
#         listOfTwittNames.append(twittText)

    return jsonify(count)

if __name__ == "__main__":
    app.run(debug=True)