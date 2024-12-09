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
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","w")
f.write(" Hello again")
f.close()

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Hello.txt","r")
s=f.read()
print(s)
f.close()
