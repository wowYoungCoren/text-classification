import os
import random
namelist = ['时政', '体育', '家居', '股票', '房产', '游戏', '财经', '娱乐', '社会', '科技', '教育']

index = 1
all_data = []
for name in namelist:
	f = open(name+"_after_jieba.txt", 'r')
	lines = f.readlines()
	print(len(lines))
	for line in lines:
		all_data.append({"content": line, "index": index})
	f.close()
	index += 1

random.shuffle(all_data)

f_train = open("train_contents_THU.txt", "w")
f_test = open("test_contents_THU.txt", "w")

print(len(all_data))
for data in all_data:
	content = data["content"]
	if '\n' not in content:
		content = content + '\n'
	f_train.write(content)
	f_test.write(str(data["index"]) + '\n')

f_train.close()
f_test.close()