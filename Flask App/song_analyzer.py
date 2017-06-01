'''Imports'''
import flask
from flask import Flask
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
import random
import sys
import json

'''Read in character indices'''
char_indices = pickle.load(open("char_indic_100.json", "rb"))
indices_char = pickle.load(open("indic_char_100.json", "rb"))

'''Run RNN'''
maxlen = 20

model = Sequential()
model.add(LSTM(512, return_sequences=True, input_shape=(maxlen, len(char_indices))))
model.add(Dropout(0.2))
model.add(LSTM(512, return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(len(char_indices)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
model.load_weights("weights.h5")

'''RNN helper function'''
def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

'''Start of the app'''
app = Flask(__name__)

'''Homepage that opens the lyrics.html file'''
@app.route('/')
def seed_input():
    with open("lyrics.html", "r") as home:
        return home.read()

'''Analysis page that finishes running the neural net'''
@app.route('/song', methods = ['POST'])
def analyze_data():

'''Gets the input data from lyrics.html'''
    form = flask.request.form
'''Prints the form in the terminal -- it prints as an immutable dictionary'''
    print(form)

'''Converts immutable dictionary to dictionary'''
    form_dict = form.to_dict()

'''Prints dictionary'''
    print(form_dict)

'''Pulls the "value" from the dictionary which is the title that the user input'''
    data = form_dict['title']
    print(data)

'''Writes the song'''
    generated = ''
    start_index = 0
    print(start_index)
    print(maxlen)
    sentence = data[start_index:start_index + maxlen]
    generated += sentence

    for i in range(400):
        x = np.zeros((1, maxlen, len(char_indices)))
        for t, char in enumerate(sentence):
            x[0, t, char_indices[char]] = 1.

        preds = model.predict(x, verbose=0)[0]
        diversity = 1.0
        next_index = sample(preds, diversity)
        next_char = indices_char[next_index]

        generated += next_char
        sentence = sentence[1:] + next_char

        sys.stdout.write(next_char)

    val = generated

    result = {"generated": val}
'''Returns the written song'''
    return generated


if __name__== '__main__':
    app.run()
