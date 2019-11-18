# -*- coding: utf-8 -*-
from numpy import mean
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


# тестовые данные:
text_data = ['good', 'bad', 'ugly', 'Beautifull', 'Brilliant', 'Super']


def semantic_res(text_data):

    semi_result = {'neg': [], 'neu': [], 'pos': []}

    for sentence in text_data:

        ss = SentimentIntensityAnalyzer().polarity_scores(sentence)

        semi_result['neg'].append(ss['neg'])
        semi_result['neu'].append(ss['neu'])
        semi_result['pos'].append(ss['pos'])
        # semi_result['compound'].append(ss['compound'])

    neg = mean(semi_result['neg'])
    neu = mean(semi_result['neu'])
    pos = mean(semi_result['pos'])

    summ = neg + neu + pos

    try:
        result = {
            'neg': int(neg / summ * 100),
            'neu': int(neu / summ * 100),
            'pos': int(pos / summ * 100),
        }
    except: # при условии что есть проблемы со входящими данными
        result = {
                    'neg': 0,
                    'neu': 0,
                    'pos': 0,
                 }

    del semi_result

    return result


if __name__ == '__main__':
    print(semantic_res(text_data))