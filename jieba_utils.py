# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:55:50 2022

@author: Takodachi
"""

import jieba
import numpy as np

jieba.load_userdict('./userdict.txt')

def get_stopword_list(file):
    """
    讀取停用txt
    """
    with open(file, encoding='utf-8')as f:
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list

def tokenize(sentence):
    """
    回傳已切割陣列
    """
    jieba.set_dictionary("dict.txt")
    stop = get_stopword_list("stop.txt")
    jie = list(jieba.cut(sentence))
    list_difference = [element for element in jie if element not in stop]
    return list_difference



  
def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    example:
    sentence = ["早安", "我", "有", "冰淇淋"]
    words = ["嗨", "早安", "我", "你", "再見", "謝謝", "好嗎"]
    bog   = [  0 ,    1 ,    1 ,   0 ,    0 ,    0 ,      0]
    """
    sentence_words = [word for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
       if w in sentence_words: 
           bag[idx] = 1
    return bag


"""
sentence = ["早安", "我", "有", "冰淇淋"]
words = ["嗨", "早安", "我", "你", "再見", "謝謝", "好嗎"]
test = bag_of_words(sentence, words)
"""


