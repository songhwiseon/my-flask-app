import pandas as pd
from konlpy.tag import Mecab
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# 1. 데이터 로드
def load_data():
    train_data = pd.read_csv("other/ratings_train.txt", sep='\t').dropna()
    test_data = pd.read_csv("other/ratings_test.txt", sep='\t').dropna()
    return train_data, test_data

# 2. 데이터 전처리
def preprocess_text(text, tokenizer):
    mecab = Mecab()
    tokens = mecab.morphs(text)
    return ' '.join(tokens)

def preprocess_data(train_data, test_data):
    mecab = Mecab() # 형태소 분석기
    train_data['document'] = train_data['document'].apply(lambda x: ' '.join(mecab.morphs(x)))
    test_data['document'] = test_data['document'].apply(lambda x: ' '.join(mecab.morphs(x)))
    return train_data, test_data



