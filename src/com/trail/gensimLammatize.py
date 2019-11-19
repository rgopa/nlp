# from gensim import utils
# lml = utils.Lemmatizer()
#  docs = ['quick brown fox', 'slow yellow tortoise', 'document nr. three']
#  for doc in docs:
#      print lm.feed(doc) # feed the documents into the parser, to be processed in parallel
# -2939683893812816931
# 5130064701692321566
# -1045879559712133929
#  lm.read()
# (5130064701692321566, ['slow/JJ', 'yellow/JJ', 'tortoise/NN'])
#  lm.read()
# (-2939683893812816931, ['quick/JJ', 'brown/JJ', 'fox/NN'])
#  lm.read()
# (-1045879559712133929, ['document/NN', 'nr/NN'])

from gensim.utils import lemmatize
print(lemmatize("Hello world!"))