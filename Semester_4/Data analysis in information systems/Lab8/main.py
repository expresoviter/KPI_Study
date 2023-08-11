from json import dump
import spacy
import re
from nltk.tokenize import sent_tokenize
import pandas as pd
from math import log10


def write(data, path):
    with open(path, 'w') as f:
        dump(data, f, ensure_ascii=False)


def lemmatize(text, nlp, v=0):
    stop_words = nlp.Defaults.stop_words
    lemmatized_words = [doc.lemma_ for doc in nlp(text)]
    if v == 1:
        print("\nTokenized text by words:\n", [doc for doc in nlp(text)])
        print("\nLemmatized text:\n", lemmatized_words)

    return [word for word in lemmatized_words if word not in stop_words and re.match(r'\w+', word)]





if __name__ == '__main__':
    with open("text1.txt") as f:
        text = f.read()
    nlp = spacy.load('uk_core_news_sm')
    sentences = sent_tokenize(text, language="russian")
    print("Tokenized text by sentences:\n", sentences)

    tokens = lemmatize(text, nlp, 1)
    write(tokens, "tokenized.json")


    def createBOW(tokens):
        dictionary = dict()
        for w in tokens:
            if w not in dictionary:
                dictionary[w] = tokens.count(w)
        return dictionary
    BOW = createBOW(tokens)
    write(BOW, "bagOfWords.json")
    frequentTen = sorted(BOW.items(), key=lambda x: x[1], reverse=True)[:10]
    print(frequentTen)

    print('Number of words in the corpus:', sum(BOW.values()))
    tf = []
    for i in range(len(sentences)):
        sentence = lemmatize(sentences[i], nlp)
        tfi = []
        for j in frequentTen:
            tfi.append(sentence.count(j[0]) / len(sentence))
        tf.append(tfi)

    idf = []
    for i in frequentTen:
        k = 0
        for j in range(len(sentences)):
            if i[0] in lemmatize(sentences[j], nlp):
                k += 1
        idf.append(log10(len(sentences) / k))

    for i in range(len(sentences)):
        for j in range(10):
            tf[i][j] = tf[i][j] * idf[j]
    data = pd.DataFrame(tf, columns=[i[0] for i in frequentTen])
    print(data.head())
    data.to_csv("result.csv")
