#coding:utf-8
import keras
import os
import tensorflow as tf
import pdb
os.environ["CUDA_VISIBLE_DEVICES"] = "0, 1"

VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 300
VALIDATION_SPLIT = 0.16
TEST_SPLIT = 0.2


print("Step 1")
train_texts = open('train_contents.txt').read().split('\n')
train_labels = open('train_labels.txt').read().split('\n')
test_texts = open('test_contents.txt').read().split('\n')
test_labels = open('test_labels.txt').read().split('\n')
all_texts = train_texts + test_texts
all_labels = train_labels + test_labels


print("Step 2")
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np

tokenizer = Tokenizer()
"""
Text tokenization utility class.

    This class allows to vectorize a text corpus, by turning each
    text into either a sequence of integers (each integer being the index
    of a token in a dictionary) or into a vector where the coefficient
    for each token could be binary, based on word count, based on tf-idf...
"""
tokenizer.fit_on_texts(all_texts)                   # fit文本列表, required before method `texts_to_sequences` or `texts_to_matrix`
sequences = tokenizer.texts_to_sequences(all_texts) # 将texts转化为interger序列
word_index = tokenizer.word_index                   # word对应index的字典，example {'东岸': 11465, '三亚机场': 43974}

print('Found %s unique tokens.' % len(word_index))
data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)
# Pads sequences to the same length. 在前面补0将每个sequence的长度统一
labels = to_categorical(np.asarray(all_labels))
# Converts a class vector (integers) to binary class matrix. 将标签转化为数组，如7 -> [0,0,0,0,0,0,0,1,0,0,0,0]
print('Shape of data tensor:', data.shape)
print('Shape of label tensor:', labels.shape)
pdb.set_trace()
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
# 根据SPLIT设置的比例分割测试集、训练集、验证集

print("Step 4: training model...")
from keras.layers import Dense, Input, Flatten, Dropout
from keras.layers import Conv1D, MaxPooling1D, Embedding, GlobalMaxPooling1D
from keras.models import Sequential
from keras import optimizers
# from keras.utils import plot_model

model = Sequential()
model.add(Embedding(len(word_index) + 1, EMBEDDING_DIM, input_length=MAX_SEQUENCE_LENGTH))
# Embedding层，实际上是一个矩阵相乘，用来文本降维 https://blog.csdn.net/weixin_42078618/article/details/82999906
# output_shape == (None, 100, 300)
model.add(Dropout(0.2))
# Dropout层，为了防止模型过拟合，训练时随机让网络某些隐含层节点的权重不工作 https://www.cnblogs.com/tornadomeet/p/3258122.html
# output_shape == (None, 100, 300)
model.add(Conv1D(250, 3, padding='valid', activation='relu', strides=1))
# 一维卷积
# output_shape == (None, 98, 250)
model.add(MaxPooling1D(3))
# 一维池化层
# output_shape == (None, 32, 250)
model.add(Flatten())
# ```python
#         model = Sequential()
#         model.add(Conv2D(64, (3, 3),
#                          input_shape=(3, 32, 32), padding='same',))
#         # now: model.output_shape == (None, 64, 32, 32)
#
#         model.add(Flatten())
#         # now: model.output_shape == (None, 65536)
#     ```
# Flatten层用来将输入“压平”，即把多维的输入一维化，常用在从卷积层到全连接层的过渡。
# https://blog.csdn.net/program_developer/article/details/80853425
# output_shape == (None, 8000)
model.add(Dense(EMBEDDING_DIM, activation='relu'))
# 全连接层
# output_shape = (None, 300)
model.add(Dense(labels.shape[1], activation='softmax'))
# output_shape = (None, 12)， 12即为分类结果的向量的长度，12 = 11 + 1
model.summary()
# Prints a string summary of the network. 打印网络详情


# plot_model(model, to_file='model.png',show_shapes=True)
# from sklearn import metrics



# sgd = optimizers.SGD(lr=3, decay=1e-6, momentum=0.9, nesterov=True)
# adagrad = keras.optimizers.Adagrad(lr=5, epsilon=None, decay=0.0)

model.compile(loss='categorical_crossentropy',
              optimizer="adamax",
              metrics=['acc', "recall", "precision", "f1score"])
#　Configures the model for training.

# model.load_weights("cnn.h5")


model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=2, batch_size=128)
# 开始训练

model.save('cnn.h5')
# 模型保存

print("Step 5: testing model...")
print(model.metrics_names)
print(model.evaluate(x_test, y_test))
# 测试结果report
        




