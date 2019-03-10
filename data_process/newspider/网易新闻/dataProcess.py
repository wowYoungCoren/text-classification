import json 
import jieba.posseg as pseg
from json.decoder import JSONDecodeError

docs = open('sportsnews.txt')
f2 = labels = open('sports_labels.txt','a')

docs_lines = docs.read().split('\n')

train = []
for doc in docs_lines:
    try:
        text = json.loads(doc)['content']
        print(text)
        if text == "":
            continue
        
        text = text[:100]
        words = pseg.cut(text)
        line0 = [] 
        for w in words:
            if 'x' != w.flag:
                line0.append(w.word)
        train.append(' '.join(line0)) 
        f2.write('5'+'\n')
    except JSONDecodeError as e:
        print(doc+'cuowu')

f1 = open('sports_tests.txt','w')
f1.write('\n'.join(train))
f1.close()