
text = """Jordan, an Arab nation on the east bank of the Jordan River, is defined by ancient monuments, 
nature reserves and seaside resorts. It’s home to the famed archaeological site of Petra, 
the Nabatean capital dating to around 300 B.C. Set in a narrow valley with tombs, temples 
and monuments carved into the surrounding pink sandstone cliffs,
 Petra earns its nickname, the "Rose City." """
from nltk.tokenize import word_tokenize,sent_tokenize
from gensim.utils import tokenize
from spacy.lang.en import English
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df = pd.DataFrame({'text':text}, index=['text'])
cv = CountVectorizer()
cv_matrix= cv.fit_transform(df['text'])
df2 = pd.DataFrame(cv_matrix.toarray(), index=['text'],columns=cv.get_feature_names_out())
print(f"{df2}")
'''
nlp=English()
print(list(word_tokenize(text)))
print(list(sent_tokenize(text)))
print(list(tokenize(text)))
print(list(nlp(text)))

'''