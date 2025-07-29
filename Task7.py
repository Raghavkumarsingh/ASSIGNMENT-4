try:
    file1 = open("D:\personal\study\code\code_file_input\Sample.txt",'r+')
    reading_file=file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
        print("Error: File 'D:\personal\study\code\code_file_input\Sample.txt' was not found.")