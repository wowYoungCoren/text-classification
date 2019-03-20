import os

no_list = ['./彩票', './时尚', './星座']
for root, dirs, files in os.walk('.', topdown=True):
	if len(files) == 0:
		continue
	if root in no_list:
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
		# if i == 100:
		# 	break
	f.close()
