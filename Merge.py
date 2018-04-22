#2 Merging

list_1 = open('./list1.txt').read().splitlines()
list_2 = open('./list2.txt').read().splitlines()
list_3 = open('./list3.txt').read().splitlines()
list_4 = open('./list4.txt').read().splitlines()
list_5 = open('./list5.txt').read().splitlines()
list_6 = open('./list6.txt').read().splitlines()
list_7 = open('./list7.txt').read().splitlines()
list_8 = open('./list8.txt').read().splitlines()

file3 = open('./results2.txt', 'w');

i1=0;
i2=0;
i3=0;
i4=0;
i5=0;
i6=0;
i7=0;
i8=0;


file_lists = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8

mylist = sorted(set(file_lists));

for item in mylist:
  file3.write("%s\n" % item);


file3.close()
