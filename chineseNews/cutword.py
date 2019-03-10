import jieba
import codecs
import re
from collections import Counter
import numpy as np

inputwords_file = "IT4.csv"
stopwords_file = "stopwords.dat"


# 读取文件
def readfile(filepath):
    fp = codecs.open(filepath, "r", encoding="utf-8")
    content = fp.read()
    fp.close()
    return content


# 保存文件
def savefile(savepath, llcontent):
    fp = codecs.open(savepath, "w", encoding='utf-8')
    for lcontent in llcontent:
        for content in lcontent:
            fp.write(content)
            fp.write(' ')
        fp.write('\n')
    fp.close()


# 按行加载文件
def readwordslist(filepath):
    wordslist = readfile(filepath).splitlines()
    return wordslist


# 去除输入文本中的网址数据
# 顺便把换行符和空格符也去了
def filter_url_tag(urlstring):
    results = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
    return results.sub("", urlstring).replace('\n', '').replace(' ', '').replace(u'\u2605', '').replace('10', '')

result = []
cutwordslist = []
stopwords = readwordslist(stopwords_file)

for url_line in readwordslist(inputwords_file):
    temp = []
    line = filter_url_tag(url_line)
    temp += [word for word in jieba.cut(line, cut_all=False) if word not in stopwords]
    cutwordslist += temp
    result.append(temp)

# "+="是两个list融合，result是list中保存list

savefile('final.txt', result)
cutwords = dict(Counter(cutwordslist))

outputwords = {}
for k, v in cutwords.items():
    if k in outputwords.keys():
        outputwords[k] += v
    else:
        outputwords[k] = v

outputwords_sorted = sorted(outputwords.items(), key= lambda x : x[1], reverse=True)[:100]

# print outputwords_sorted
# 使输出能正常显示中文字符
print(repr(outputwords_sorted))
print("")
print(np.shape(outputwords_sorted))

# file = open('IT4.csv', encoding='utf-8').read().split('\n')  # 一行行的读取内容
# Rs2 = []  # 建立存储分词的列表
# for i in range(len(file)):
#     temp = file[i].strip().replace("\u3000", "").replace("月", "").replace("日", "")
#     temp_nodigit = ''.join([i for i in temp if not i.isdigit()])
#     result = []
#     seg_list = jieba.cut(temp_nodigit)
#     for w in seg_list:  # 读取每一行分词
#         result.append(w)
#     Rs2.append(result)  # 将该行分词写入列表形式的总分词列表
#
# # 写入CSV
# newfile = open('result.csv', 'w', encoding='utf-8')
# writer = csv.writer(newfile)  # 定义写入格式
# writer.writerows(Rs2)  # 按行写入
# # file.write(str(Rs))
# newfile.close()