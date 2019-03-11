#coding:utf-8
import keras
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0, 1"

VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 300
VALIDATION_SPLIT = 0.16
TEST_SPLIT = 0.2


print("Step 1")
train_texts = open('train_contents.txt').read().split('\n')
train_labels = open('train_labels.txt').read().split('\n')
test_texts = open('./data_process/newspider/网易新闻/sports_tests.txt').read().split('\n')
test_labels = open('./data_process/newspider/网易新闻/sports_labels.txt').read().split('\n')
all_texts = train_texts + test_texts
all_labels = train_labels + test_labels


print("Step 2")
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np

tokenizer = Tokenizer()
tokenizer.fit_on_texts(all_texts)
sequences = tokenizer.texts_to_sequences(all_texts)
word_index = tokenizer.word_index

print('Found %s unique tokens.' % len(word_index))
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
labels = to_categorical(np.asarray(all_labels))
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)

# import random
# a = random.Random()
# a.seed(10)
# a.shuffle(data)
# a.shuffle(labels)

print("Step 3")
# split the data into training set, validation set, and test set
p1 = int(len(data)*(1-VALIDATION_SPLIT-TEST_SPLIT))
p2 = int(len(data)*(1-TEST_SPLIT))
x_train = data[:p1]
y_train = labels[:p1]
x_val = data[p1:p2]
y_val = labels[p1:p2]
x_test = data[p2:]
y_test = labels[p2:]
print('train docs: '+str(len(x_train)))
print('val docs: '+str(len(x_val)))
print('test docs: '+str(len(x_test)))


print("Step 4: training model...")
from keras.layers import Dense, Input, Flatten, Dropout
from keras.layers import Conv1D, MaxPooling1D, Embedding, GlobalMaxPooling1D, CuDNNLSTM
from keras.models import Sequential
from keras import optimizers, metrics
# from keras.utils import plot_model

model = Sequential()
model.add(Embedding(len(word_index) + 1, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
model.add(CuDNNLSTM(EMBEDDING_DIM))
# model.add(Dropout(0.2))
model.add(Dense(EMBEDDING_DIM, activation='relu'))
model.add(Dense(labels.shape[1], activation='softmax'))
model.summary()
# plot_model(model, to_file='model.png',show_shapes=True)

# sgd = optimizers.SGD(lr=3, decay=1e-6, momentum=0.9, nesterov=True)
# adagrad = keras.optimizers.Adagrad(lr=5, epsilon=None, decay=0.0)
model.compile(loss='categorical_crossentropy',
              optimizer="rmsprop",
              metrics=['acc', 'recall', 'precision', 'f1score'])

# model.load_weights("cnn.h5")


model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=3, batch_size=128)
model.save('cnn.h5')

print("Step 5: testing model...")
print(model.metrics_names)
# model.metrics
print(model.evaluate(x_test, y_test))