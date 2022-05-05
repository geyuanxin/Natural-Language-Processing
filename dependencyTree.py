
#%%
import stanfordnlp
from stanfordcorenlp import StanfordCoreNLP
#!pip install stanfordnlp
#!pip install stanfordcorenlp

nlp = StanfordCoreNLP(r'C:\stanford-corenlp-4.4.0',lang='en')
sentence="FRIZZY PANICLE (FZP), an essential gene that controls spikelet differentiation and development in the grass family (Poaceae), prevents the formation of axillary bud meristems and is closely associated with crop yields."
print(nlp.word_tokenize(sentence))
from nltk.parse import corenlp
from nltk.tree import Tree
parser = corenlp.CoreNLPParser(url='http://localhost:9000')
res = parser.parse_text(sentence)
for i in res:
    Tree.convert(i).draw()