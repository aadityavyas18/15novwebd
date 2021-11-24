#Q8
def pangram(s):
    check=""
    small=s.lower()
    combine=small.replace(" ","")
    for i in combine:
        if i in check:
            return False
        else:
            check+=i
    return True
print(pangram("hola this is python"))
#Q9
n=int(input('enter the integer:'))
a1=n
a2=(n*n)
a3=(n*n*n)
print(a1+a2+a3)
#Q10
s=input("Enter a string")
l=s.split("#")
x=l[0].split(' ')
for i in range(len(x)):
    x[i]=int(x[i])
y=l[1].split(' ')
for i in range(len(y)):
    y[i]=int(y[i])
print(x)
print(y)
#q11
sentence=input("Input words")
Input wordswithout,hello,bag,world
sentence_list=sentence.split(",")
sentence_list.sort()
print((',').join(sentence_list))
#Q12
d = {'Student': ['abc','aaditya','ansh','arpit'], 'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i

d2=d['Student']
print(d2[j])


#Q 13
s5=input("Enter a string:")
l=0
d=0
for i in s5:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("LETTERS ",l)
print("DIGITS ",d)


#Q14
d = {'Name': ['Akshay', 'aaditya', 'soni' , 'Anil', 'mehul', 'harsh'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l1=d['Name']
l2=[]
l3=[]
l4=d['Ratings']
l5=[]
sub=d['Subject']
for i in range(len(sub)):
    if sub[i]==s:
        l2+=[sub[i]]
        l3+=[l1[i]]
        l5+=[l4[i]]
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)
      
