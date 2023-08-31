import emoji
import nltk
from pandas import DataFrame
from re import sub


STOPWORDS = nltk.corpus.stopwords.words('portuguese')
REGEX = [
    {'input': r'https?[^\s]*', 'output': r' '},
    {'input': r'([!-/<=>bdghj-nqtv-à-õ])\1+', 'output': r'\g<1>'},
    {'input': r'([aiu])\1+', 'output': r'\g<1>'},
    {'input': r'(([rscp])\2)\2+', 'output': r'\g<1>'},
    {'input': r'@[A-Za-z0-9$-_@.&+]+', 'output': r' '},
    {'input': r'[!-/:-@\[-`{-~•]', 'output': r' '},
    {'input': r'\n', 'output': r' '},
    {'input': r'\d+', 'output': r' '},
    {'input': r'\s+', 'output': r' '},
]


class Preprocess():

    def regexTreatment(self, data):
        for reg in REGEX:
            data = sub(reg.get('input'), reg.get('output'), data)
        return data

    def stopwordsTreatment(self, data):
        data_without_stopwords = [word for word in data.split() if word not in (STOPWORDS)]
        return ' '.join(data_without_stopwords)

    def emojiTreatment(self, data):
        return emoji.replace_emoji(data, replace='')

    def lengthTreatment(self, data):
        important_words = [word for word in data.split() if len(word) > 2]
        return ' '.join(important_words)

    def preprocessData(self, data: DataFrame):
        data['item'] = data['item'].str.lower().apply(lambda x: self.stopwordsTreatment(x))
        data['item'] = data['item'].str.lower().apply(lambda x: self.emojiTreatment(x))
        data['item'] = data['item'].str.lower().apply(lambda x: self.regexTreatment(x))
        data['item'] = data['item'].apply(lambda x: self.lengthTreatment(x))
        return data