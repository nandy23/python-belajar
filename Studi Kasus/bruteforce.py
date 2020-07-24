import string

flag = [233, 129, 9, 5, 130, 194, 195, 39, 75, 229]
for i in range(len(flag)):
    for char in string.printable:
        a = (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255
        if (a == flag[i]):
            print(a)
            print(char)
        
        #if (user_str[i] == flag[i]) :
            #print(char)
