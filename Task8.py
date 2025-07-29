file1 = open("D:\personal\study\code\code_file_input\output.txt",'w')
word_adding=input("Enter test to write to the file:")
writing_file=file1.write(word_adding)
file1.close()

file1 = open("D:\personal\study\code\code_file_input\output.txt",'r')
reading_file=file1.read()
print(reading_file,"\ndata successfully written to output.txt")
file1.close()

file1 = open("D:\personal\study\code\code_file_input\output.txt",'a')
appending_file=file1.write("\nLearing file handling in Python")
print("\nLearing file handling in Python\ndata successfully append")
file1.close()

file1 = open("D:\personal\study\code\code_file_input\output.txt",'r')
reading_file=file1.read()
print(reading_file)
file1.close()



