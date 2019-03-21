import os
import time

start = time.time()
namelist = ['时政', '体育', '家居', '股票', '房产', '游戏', '财经', '娱乐', '社会', '科技', '教育']
for root, dirs, files in os.walk('.', topdown=True):
	start_inside = time.time()
	if root[2:] not in namelist:
		continue
	f = open(root+'.txt', 'w')
	for i, file in enumerate(files):
		file_path = os.path.join(root, file)
		fr = open(file_path, 'r')
		lines = fr.readlines()
		write_content = ''
		for line in lines:
			line = line.strip("\n")
			line = line.strip("\u3000")
			write_content += line	
		f.write(write_content + '\n')
		fr.close()
		if i == 20000:
			break
	f.close()
	print(root[2:]+" DONE")
	print(root[2:]+" USE TIME: ", time.time()-start_inside)
print("ALL_DONE")
print("USE TIME: ", time.time() - start)