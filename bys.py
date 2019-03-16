# coding:utf-8
VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 200
TEST_SPLIT = 0.2


print('(1) load texts...')
train_texts = open('train_contents.txt').read().split('\n')
train_labels = open('train_labels.txt').read().split('\n')
test_texts = open('./data_process/newspider/今日头条/testdata/testdata.txt').read().split('\n')
test_labels = open('./data_process/newspider/今日头条/testdata/testlabel.txt').read().split('\n')
all_text = train_texts + test_texts
# 加载文件

print('(2) doc to var...')
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer   
count_v0 = CountVectorizer()
# 将文本数据转化成特征向量的过程, 此为词袋法，只考虑词总的出现次数
counts_all = count_v0.fit_transform(all_text)
# 先使用全部的text生成词汇表，储存在vocabulary_属性
count_v1 = CountVectorizer(vocabulary=count_v0.vocabulary_)
# 使用所有text生成的词汇表做mapping，初始化对象
"""
vocabulary参数：
vocabulary : Mapping or iterable, optional
        Either a Mapping (e.g., a dict) where keys are terms and values are
        indices in the feature matrix, or an iterable over terms. If not
        given, a vocabulary is determined from the input documents. Indices
        in the mapping should not be repeated and should not have any gap
        between 0 and the largest index.
"""
counts_train = count_v1.fit_transform(train_texts)
# 使用刚初始化的对象生成trian集的特征向量，为什么要这样做： 将测试集特征与训练集关联，如果词与indices不对应的话，就无法进行测试
print("the shape of train is "+repr(counts_train.shape))
count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_)
counts_test = count_v2.fit_transform(test_texts)
# 与上面相同
print("the shape of test is "+repr(counts_test.shape))

tfidf_transformer = TfidfTransformer()
train_data = tfidf_transformer.fit(counts_train).transform(counts_train)
# 使用tfidf生成特征向量，关注在词在某一类中出现的频率，考虑词能否很好表示类别
test_data = tfidf_transformer.fit(counts_test).transform(counts_test)

x_train = train_data
y_train = train_labels
x_test = test_data
y_test = test_labels

print('(3) Naive Bayes...')
from sklearn.naive_bayes import MultinomialNB  
from sklearn import metrics
clf = MultinomialNB(alpha = 0.01)   
clf.fit(x_train, y_train)
# Fit Naive Bayes classifier according to X, y, x为数据向量，y为标签， 进行训练

preds = clf.predict(x_test)
# Perform classification on an array of test vectors X. x为数据向量， 进行测试

preds = preds.tolist()
target_names = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11']
print(metrics.classification_report(y_test, preds, digits=10))
# sklearn测试report

# num = 0
# for i, pred in enumerate(preds):
#     if int(pred) == int(y_test[i]):
#         num += 1
# print('precision_score:' + str(float(num) / len(preds)))





        




