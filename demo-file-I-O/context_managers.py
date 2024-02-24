with open("test_2.txt", 'a') as file:   # Here the file is opening for writing with context manager. [with]
    for i in range(0,100):              # This way will automatically exit from for loop, when the writing completed.   
        file.write(str(i) + '\n')
