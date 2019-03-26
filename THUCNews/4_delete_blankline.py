t1 = open('test_labels_THU.txt').read()
len(t1)
t4 = open('test_labels_final.txt','w')
t4.write(t1[:-1])
t4.close()

t2 = open('test_contents_THU.txt').read()
len(t2)
t3 = open('test_contents_final.txt','w')
t3.write(t2[:-1])
t3.close()


t01 = open('train_labels_THU.txt').read()
len(t01)
t02 = open('train_contents_THU.txt').read()
len(t02)
t03 = open('train_contents_final.txt','w')
t03.write(t02[:-1])
t03.close()
t04 = open('train_labels_final.txt','w')
t04.write(t01[:-1])
t04.close()

