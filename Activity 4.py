file1=open('Codingal.txt','r')
file2=open('UpdatedFile.txt','w')

cont=file1.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if i%2!=0:
      file2.write(cont[i-1])
    else:
      pass

file1.close()
file2.close()
