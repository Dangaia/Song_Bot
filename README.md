**Botley Crue**

If you've listened to any popular music in the last n years you've probably noticed that they are written by 6 year olds.

See: Work by Rihanna. Here, now you don't even have to look it up.

https://www.youtube.com/watch?v=HL1UzIK-flA

For this project I decided to create a bot/app that can write its own songs. The data came from a CSV on Kaggle of > 50,000 lyrics. To accomplish this I used Markov Chains and Long Short Term Memory Recurrent Neural Networks.

In this repo I have all my presentation, IPython notebooks, JSON files, weights, and Flask App files organized by folder.

***Folders***

1. __Presentation__
  - PDF of presentation

2. __Notebooks__

  - _Data Cleaning_
    - Where all of my data was cleaned

  - _Markov Chains_
    - Code for the creation of songs using Markov Chains

  - _RNN_
    - Code for the training of songs using Recurrent Neural Networks

  - _RNN Song Writer_
    - Code for the actual writing of the songs using the Recurrent Neural Network

  - _Unsupervised Learning_
    - Part of this project included doing some portion of unsupervised learning. This is where I did vectorization, graphing, and topic modeling. This data wasn't used for the project presentation.

3. __Flask App__

  - _song_analyzer.py_

    - My flask app
    - This file references the *lyrics.html* file also in this folder
    - The neural net actually runs in this file

  - _lyrics.html_
    - The actual html file of the flask app

4. __JSON Files__

  - _char_indic_100.json_ & _indic_char_100.json_
    - Character indices files from model trained on a 100,000 length slice of all of the lyrics (mostly ABBA songs)

  - _char_indic.json_ & _indic_char.json_
    - Character indices files from model trained on all lyrics

  - _arch.json_ & _test.json_
    - Other json files needed to run the neural net

5. __Pickle Files__

  - _corpus.p_
    - Corpus of all lyrics
    - Used in *Markov Chains* notebook

  - _flat_lyrics.p_
    - Flattened version of all lyrics
    - Used in *Unsupervised Learning* notebook

  - _flat_test.p_
    - Slice of flattened version of all lyrics
    - Used in *Unsupervised Learning* notebook

  - _lyrics_text.p_
    - String of all lyrics
    - Used in *RNN* notebook

  - _split_test.p_
    - Sliced string of all lyrics
    - I don't think this is actually used in any of the notebooks other than *Data Cleaning*

6. __Weight Files__

  - _weights.h5_
    - Weights created by sliced version of RNN

  - _test_weights.h5_
    - Weight created by full version of RNN

The end.
