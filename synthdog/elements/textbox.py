"""
 Donut
 Copyright (c) 2022-present NAVER Corp.
 MIT License
"""
import numpy as np
from synthtiger import layers
from pythainlp.tokenize import word_tokenize

class TextBox:
    def __init__(self, config):
        self.fill = config.get("fill", [1, 1])

    def generate(self, size, text, font):
        width, height = size

        char_layers, words = [], []
        fill = np.random.uniform(self.fill[0], self.fill[1])
        width = np.clip(width * fill, height, width)
        font = {**font, "size": int(height)}
        left, top = 0, 0
        new_text = ""
        counter = 0
        for char in text:
            if char in "\r\n":
                continue
            if counter > width:
                break
            new_text += char
            counter+=1
        #print("new_text",new_text)
        for word in word_tokenize(new_text, engine="newmm"):
            if word in "\r\n":
                continue
            #print("word",word)
            word_layer = layers.TextLayer(word, **font)
            word_scale = height / word_layer.height
            word_layer.bbox = [left, top, *(word_layer.size * word_scale)]

            if word_layer.right > width:
                break

            char_layers.append(word_layer)
            words.append(word)
            left = word_layer.right

        text = "".join(words).strip()
        if len(char_layers) == 0 or len(text) == 0:
            return None, None
        #print("text and char_layers",text,char_layers)
        text_layer = layers.Group(char_layers).merge()

        return text_layer, text
    
