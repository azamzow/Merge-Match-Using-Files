#1 Matching

list_1 = open('./list1.txt').read().splitlines()
list_2 = open('./list2.txt').read().splitlines()

file3 = open('./results.txt', 'w');

i1=0;
i2=0;

while i1 != 11:

    name_1 = list_1[i1];
    name_2 = list_2[i2];

    if name_1 < name_2:
        i1 = i1 + 1;
        
    elif name_1 > name_2:
        i2 = i2 + 1;
    
    elif name_1 == name_2:
        file3.write(name_1);
        file3.write("\n");
        i1 = i1 + 1;
        i2 = i2 + 1;
    else:
        break

    
file3.close()
