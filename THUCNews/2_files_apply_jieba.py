#coding:utf-8
import jieba.posseg as pseg
import os

WORD_LEN = 100

def jieba(name):
    contents = open(name + '.txt', 'r')
    read_lines = contents.read().split('\n')

    train = []
    test = []

    num = 0

    for line in read_lines:
        num += 1
        if num%10000 == 0:
            print(num)
        words = pseg.cut(line)
        line0 = []
        for w in words:
            if 'x' != w.flag:
                line0.append(w.word)
            if len(line0) == WORD_LEN:
                break
        train.append(' '.join(line0))
        # if num == 100:
        #     break
    contents.close()
    fw = open(name + '_after_jieba.txt','w')
    fw.write('\n'.join(train))
    fw.close()

if __name__ == '__main__':
    namelist = ['时政', '体育', '家居', '股票', '房产', '游戏', '财经', '娱乐', '社会', '科技', '教育']
    for name in namelist:
        jieba(name)
    print("DONE")