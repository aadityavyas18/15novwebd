Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5**9
1953125
3//2
1
7//3
2
7/3
2.3333333333333335
6==6
True
a=20
a+=30
a%=3
print(a)
2
True * False
0
True & False
False
True and False
False
((6>3)and(7>4) or (18==3)) and (9>3)
True
((6>3)and(7<4) or (18==3)) and (9>3)
False
True is False
False
False in 'False'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    False in 'False'
TypeError: 'in <string>' requires string as left operand, not bool
((True==False) or (False > True)) and (False<=True)
False
#Q3
s1="nice to have it"
s2="here"
s=s1+" "+s2
s
'nice to have it here'
#q4
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])
['hello']
#Q5
#s1 and s2 are to be inserted in a
#s1 and s2 are to be inserted in a so
a[:0]=[str(s1)]
a.append(str(s2))
print(a)
['nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']

#Q6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]
for i in numbers:
    if(i%2==0)
    
SyntaxError: expected ':'
for i in numbers:
    if(i%2==0):
        print(i)
    elif(i==237):
        break;

386
462
418
344
236
566
978
328
162
758
918
#Q7
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print('color_test_1'-'color_test_2')


