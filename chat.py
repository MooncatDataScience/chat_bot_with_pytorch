# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 08:32:02 2022

@author: Takodachi
"""

import random
import json
import torch
from model import NeuralNet
from jieba_utils import bag_of_words, tokenize

device = torch.device(str("cuda:0") if torch.cuda.is_available() else "cpu") 


with open('intents.json', 'r', encoding="utf-8") as f:
    intents = json.load(f)

FILE = 'data.pth'
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data['tags']
model_state = data["model_state"]


model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "AI客服"
print("讓我們開始吧!")
while True:
    sentence = input('你: ')
    if sentence == '離開':
        break
    
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)
    
    output = model(X)
    _, predicted = torch.max(output, dim = 1)
    tag = tags[predicted.item()]
    
    probs = torch.softmax(output, dim = 1)
    prob = probs[0][predicted.item()]
    
    
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent['tag']:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: 我不明白")
        
    
    




