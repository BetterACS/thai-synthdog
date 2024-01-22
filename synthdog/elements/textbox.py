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
        self.tokenize_engine = config.get("tokenize_engine", "newmm")

    def generate(self, size, text, font):
        width, height = size

        char_layers, words = [], []
        fill = np.random.uniform(self.fill[0], self.fill[1])
        width = np.clip(width * fill, height, width)
        font = {**font, "size": int(height)}
        left, top = 0, 0
        
        sentence = ""
        character_counter = 0
        for char in text:
            if character_counter > width:
                break
            if char in "\r\n":
                continue
            sentence += char
            character_counter += 1

        for word in word_tokenize(sentence, engine=self.tokenize_engine):
            if word in "\r\n":
                continue

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

        text_layer = layers.Group(char_layers).merge()

        return text_layer, text
    
