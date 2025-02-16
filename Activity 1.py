file=open('Codingal.txt','r')
print(file.read())
file.close()

file=open('Codingal.txt','r')
print(file.read(5))
file.close()

file=open('Codingal.txt','a')
file.write("\nI am Penguin and I am 1 year old")
file.close()
