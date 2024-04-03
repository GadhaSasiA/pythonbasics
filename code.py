row=5
i=1
while i<=row:
    print('*'*i)
    i+=1


mixed_array= [1,2,3,4,6,5,6,3]
unique_array=[]
for i in mixed_array:
    if i not in unique_array:
        unique_array.append(i)
print(unique_array)

array=[1,2,3,4,5]
maximum=max(array)
minimum=min(array)
print("maximum value",maximum)
print("minimum value",minimum)


array=[1,10,2,3,4,5]
max=array[0]
min=array[0]

for i in array:
    if i <= min:
     min=i
    elif i>=max:
       max=i
       
print("minimum",min)
print("maximum",max)



list1=[] #an empty list for display elements
for i in range(0,10):# add range of numbers 
  list1.append(i)#i is index of the range (append is add)adding each index into list1
  i+=1 #to check each elements
print(list1)


list1=[] #an empty list for display elements
num=[]
for i in range(10):
  list1.append(i)
print(list1)
for i in range(10):
    list1[i] = i * (i + 1) / 2
    num.append(list1[i])
print( num)



def pattern(n):
    for i in range(0,n):
     for j in range(0,i+1):
        print("*", end='')
     print("")
n=5
pattern(n)

def my_function(n):
    num=1
    for i in range(0,n):
        for j in range(0,i+1):
            print(num,end='')
            num=num+1
        print("")
n=5
my_function(n)

def number(n):
    for i in range(0,n):
        num=1
        for j in range(0,i+1):
            print(num,end='')
            num=num+1
        print("")
n=5
number(5)

num=int(input("enter a number:"))

if num%2==0:
    print(num,"is even number")
else:
    print(num,"is odd number")


def freequency():
    string_1=input("enter a string:")
    split_word=string_1.split()
    d={}

    for i in split_word:
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
freequency()



# 

string1=input("enter a string:")
reverse=string1[::-1]
if string1==reverse:
    print(string1,"is palindrome")
else:
    print(string1,"is not a palindrome")

def palindrome(n):
    reverse=n[::-1]
    if n==reverse:
        print(n,"is palindrome")
    else:
        print(n,"is not a palindrome")
n=input("enter a string:")
palindrome(n)




def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("strings are anagram")
    else:
        print("strings are not anagram")

s1=input("enter string:")
s2=input("enter string:")
check(s1,s2)



def prime(n):
    if n<=1:
        print(n,"is not a prime number")
    else:
        for i in range(2,n):
         if n%i==0:
            print(n,"is prime number:")
            break
        else:
            print(n,"is not a prime number")
n=int(input("enter a number:"))
prime(n)
