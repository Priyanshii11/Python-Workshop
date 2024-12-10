#file handling
#f=open("C:\Users\hp\OneDrive\Desktop\Hello.txt" , "r")[error]
#f=open(r"C:\Users\hp\OneDrive\Desktop\book.txt","r")
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
st =f.read()
lst =list(st)
words=1
p=st.split(" ")
print(p)
#words
for i in range(0,len(lst)):
    if(lst[i] == " " or lst[i]== "\n"):
         words +=1
print(words)
#line
words1=1
for i in range(0,len(lst)):
    if(lst[i]== "\n"):
         words1 +=1
print(words1)
#char
words2=1
for i in range(0,len(lst)):
    if(lst[i]!= " " or lst[i]== "\n"):
         words2 +=1
print(words2)
f.close()'''
#read only single linese
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.readline()
print(s)
s2=f.readline()
print(s1)
f.close()'''

#chnage to list 
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.readlines()
print(len(s))
f.close()'''

#only specific number of lines
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.read(5)
print(len(s))
f.close()'''

#append function
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","a")
f.write(" Hello again")
f.close()'''

'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.read()
print(s)
f.close()'''

#write operaation
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","w")
f.write(" Hello again")
f.close()

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.read()
print(s)
f.close()
'''

#write list into file
'''l=['ram','hello','bye']
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","w")
f.writelines(l)
f.close()

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.read()
print(s)
f.close()'''

#copy from one file to another
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
S=f.read()
f2=open("C:\\Users\\hp\\OneDrive\\Desktop\\hello2.txt","w")
f2.write(S)
f.close()
f2.close()
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\hello2.txt","r")
s=f.read()
print(s)
f.close()'''

#copy from two file into third file
'''f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
S=f.read()
f2=open("C:\\Users\\hp\\OneDrive\\Desktop\\hello2.txt","r")
S2=f2.read()
f3=open("C:\\Users\\hp\\OneDrive\\Desktop\\h3.txt","a")
f3.write(S +" "+ S2)
f.close()
f2.close()
f3.close()
f4=open("C:\\Users\\hp\\OneDrive\\Desktop\\h3.txt","r")
s=f4.read()
print(s)
f4.close()'''

#Exception handling


