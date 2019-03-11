# coding:utf-8
VECTOR_DIR = 'vectors.bin'

MAX_SEQUENCE_LENGTH = 100
EMBEDDING_DIM = 200
TEST_SPLIT = 0.2


print('(1) load texts...')
train_texts = open('train_contents.txt').read().split('\n')
train_labels = open('train_labels.txt').read().split('\n')
test_texts = open('./data_process/newspider/网易新闻/sports_tests.txt').read().split('\n')
test_labels = open('./data_process/newspider/网易新闻/sports_labels.txt').read().split('\n')
all_text = train_texts + test_texts

print('(2) doc to var...')
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer   
count_v0 = CountVectorizer()
counts_all = count_v0.fit_transform(all_text)
count_v1 = CountVectorizer(vocabulary=count_v0.vocabulary_)
counts_train = count_v1.fit_transform(train_texts)
print("the shape of train is "+repr(counts_train.shape))
count_v2 = CountVectorizer(vocabulary=count_v0.vocabulary_)
counts_test = count_v2.fit_transform(test_texts)
print("the shape of test is "+repr(counts_test.shape))

tfidf_transformer = TfidfTransformer()
train_data = tfidf_transformer.fit(counts_train).transform(counts_train)
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
preds = clf.predict(x_test)
num = 0
preds = preds.tolist()
for i, pred in enumerate(preds):
    if int(pred) == int(y_test[i]):
        num += 1
target_names = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11']
print(metrics.classification_report(y_test, preds, digits=10))
# print('precision_score:' + str(float(num) / len(preds)))





        




