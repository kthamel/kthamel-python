file = open("test_1.txt",'w')   # Here passing a 'w' with the required file. Cause, going to write into the file.
                                # 'w' stands for *write with truncate* mode
for i in range(0, 100):
    file.write(str(i) + '\n')          # Have to convert the writing data type into strings.

file.close()