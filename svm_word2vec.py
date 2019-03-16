#coding:utf-8
VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 200
TEST_SPLIT = 0.2


print('(1) load texts...')
train_docs = open('train_contents.txt').read().split('\n')
train_labels = open('train_labels.txt').read().split('\n')
test_docs = open('test_contents.txt').read().split('\n')
test_labels = open('test_labels.txt').read().split('\n')

print('(2) doc to var...')
import gensim
import numpy as np
w2v_model = gensim.models.KeyedVectors.load_word2vec_format(VECTOR_DIR, binary=True)
x_train = []
x_test = []
for train_doc in train_docs:
    words = train_doc.split(' ')
    vector = np.zeros(EMBEDDING_DIM)
    word_num = 0
    for word in words:
        if word in w2v_model:
            vector += w2v_model[word]
            word_num += 1
    if word_num > 0:
        vector = vector/word_num
    x_train.append(vector)
# 在train_doc文件中直接取word，将有的词加入vector列表，对于没有的词不加入
# note: 不进行转化降维，直接将word2vec模型的权重值作为特征放到SVM训练
for test_doc in test_docs:
    words = test_doc.split(' ')
    vector = np.zeros(EMBEDDING_DIM)
    word_num = 0
    for word in words:
        if word in w2v_model:
            vector += w2v_model[word]
            word_num += 1
    if word_num > 0:
        vector = vector/word_num
    x_test.append(vector)
# 与上同

print('train doc shape: '+str(len(x_train))+' , '+str(len(x_train[0])))
print('test doc shape: '+str(len(x_test))+' , '+str(len(x_test[0])))
y_train = train_labels
y_test = test_labels

print('(3) SVM...')
from sklearn.svm import SVC   
svclf = SVC(kernel = 'linear')
# C-Support Vector Classification. 是SVM的一种，输入标签为分类值则用SVC()做分类
# https://blog.csdn.net/qq_41577045/article/details/79859902

svclf.fit(x_train,y_train)
# fit 进行训练

preds = svclf.predict(x_test);  
num = 0
preds = preds.tolist()
for i,pred in enumerate(preds):
    if int(pred) == int(y_test[i]):
        num += 1
print('precision_score:' + str(float(num) / len(preds)))
# 预测并report




        




