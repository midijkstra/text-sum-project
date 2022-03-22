import re
import pickle
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


encoder = (
    'English', 'French', 'Spanish', 'Portuguese', 'Italian',
    'Russian', 'Swedish', 'Malayalam', 'Dutch', 'Arabic',
    'Turkish', 'German', 'Tamil', 'Danish', 'Kannada', 'Greek', 'Hindi'
)

def preprocess(x):
    REG_STR = '[0-9\W_]'
    data = []

    for text in x:
        text = [s.strip().lower() for s in re.split(REG_STR, text) if s != '']
        text = ' '.join(text)
        data.append(text)
    
    return data


if __name__ == '__main__':

    df = pd.read_csv('LanguageDetection.csv')
    x = df['Text']
    y = df['Language']

    # Manually encode labels and prerprocess data
    y = np.array([encoder.index(a) for a in y])
    data = preprocess(x)

    # Create bags of words (save)
    vect1 = CountVectorizer()
    vect2 = TfidfVectorizer(ngram_range=(1,3), analyzer='char')
    x1 = vect1.fit_transform(x).toarray()
    x2 = vect2.fit_transform(x).toarray()
    pickle.dump(vect1, open('models\\vect1.pkl', 'wb'))
    pickle.dump(vect2, open('models\\vect2.pkl', 'wb'))

    # Train models (save)
    model1 = MultinomialNB()
    model2 = MultinomialNB()
    model1.fit(x1, y)
    model2.fit(x2, y)
    pickle.dump(model1, open('models\\model1.pkl', 'wb'))
    pickle.dump(model2, open('models\\model2.pkl', 'wb'))