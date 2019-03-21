import os
import random
namelist = ['时政', '体育', '家居', '股票', '房产', '游戏', '财经', '娱乐', '社会', '科技', '教育']

TEST_SPLIT = 0.15
index = 1
all_data = []
for name in namelist:
	f = open(name+"_after_jieba.txt", 'r')
	lines = f.readlines()
	print(name+": "+str(len(lines)))
	for line in lines:
		all_data.append({"content": line, "index": index})
	f.close()
	index += 1

random.shuffle(all_data)

f_train_content = open("train_contents_THU.txt", "w")
f_train_labels = open("train_labels_THU.txt", "w")
f_test_content = open("test_contents_THU.txt", "w")
f_test_labels = open("test_labels_THU.txt", "w")


print("alldata: "+str(len(all_data)))
devide_line = int(TEST_SPLIT * len(all_data))
test_data = all_data[:devide_line]
train_data = all_data[devide_line:]

def write_file(out_data, f_content, f_labels):
	for data in out_data:
		content = data["content"]
		if '\n' not in content:
			content = content + '\n'
		f_content.write(content)
		f_labels.write(str(data["index"]) + '\n')
	f_content.close()
	f_labels.close()

write_file(test_data, f_test_content, f_test_labels)
write_file(train_data, f_train_content, f_train_labels)