message = input("Enter the string you want to print in text file : ")
samplefile=open("C:/Users/KHUSHI/textfile.txt", 'w')
print(message,file=samplefile)