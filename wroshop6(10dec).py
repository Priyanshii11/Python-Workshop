#closure and decorator Advanced python concepts
'''def name():
    return 'Santosh'
def outer(funct):
    def inner():
        x=funct()
        return x +'Hi'
    return inner
y=outer(name)
print(y() )'''


'''def outer(funct):
    def inner():
        x=funct()
        print("Hi" ,x)
    return inner
@outer 
def name():
    return 'Priyanshi '
y=name()'''

#most important
'''def outer(funct):
    def inner(t,p):
        x=funct(t,p)
        for i in range(1,5):
            print(p ,end=" " )
        print()
        print(x.upper())
        for i in range(1,5):
            print(p ,end=" " )
    return inner
@outer
def name(text,p):
    return text
y=name('santosh','#')'''
'''#decotaer number 1
def upper(funct):
    def inner():
        x=funct()
        return x.upper()
    return inner
#decorater number 2
def listOuter(func):
    def listinner():
        x=func()
        return list(x)
    return listinner
@listOuter 
@upper 
def name():
    lst = input("enter name:")
    return lst
y=name()
print(y)'''

#decotaer number 1
'''def upper(funct):
    def inner(t):
        x=funct(t)
        return x.upper()
    return inner
#decorater number 2
def listOuter(func):
    def listinner(t):
        x=func(t)
        return list(x)
    return listinner
@listOuter 
@upper

def name(t):
    return t

lst = input("enter name:")
y=name(lst)
print(y)
'''

class myclass:
    a="hello"
obj =myclass()
print(obj.a)
