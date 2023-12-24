import random
import itertools
name=input("Enter your name:")
print("Hey "+name+"!!!,Welcome to the password generator")
x=int(input("How many numbers you want in your password:"))
num=[i for i in range(10)]
a=random.sample(num,x)
y=int(input("How many letters you want in your password:"))
alp="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
b=random.sample(alp,y)
z=int(input("How many symbols you want in your password:"))
sy="!@#$%&^*\<>?/~"
c=random.sample(sy,z)
print("This is your password as per your requirements:")
var=list(itertools.chain(a,b,c))
final=random.sample(var,len(var))
for i in range(len(final)):
    print(final[i],end="")
