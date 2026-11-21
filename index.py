print("hello world")

# comments

# print("simran")

print("python","is","awesome",sep="-");
print("python");
print("its");
print("awesome");

name = "PRITAM"
age =20 
height = 5.6 
complex_number= 2+3j
is_student = True 
print(name, age,height,complex_number,is_student, sep=","  )

print(type(name))
print(type(age))
print(type(height))
print(type(complex_number))

# a =10;
# b =20;
# c =30;
# d =40;

a,b = 10,20 
print(a,b) 

#print(a,b,,c)

temp=0;
temp =a;
a=b;
b=temp;

# type casting 

str = "25";
int1= int(str);
float1 = float(str);
str2 = (float(str));
bool1 = bool(0) ;          #0,9,"",[],set,''
print(type(str),str);

#print(bool1)

# operators 
# - 
# + 
# * 
# / 
# //
# %
# **   

print(10+20 );
print(20-10 );
print(20*20 );
print(1/2 );
print(3/2);
print(3%2);
print (3**2);
3*3

print(10==10);
print(10!=10);
print(10>10);
print(10>=10);
print(10<=10); 

#assingment perators 
#= 
#+=
#-=
#*=
#/=
#//=
#%=
#**=

x1 = 20 ;
x1+=20;
x1-=5;
x1*=2;
x1//=2;
x1%=2;
x1**=4;

print(x1)

# membership comperison
pet = "cat";
checkval = "c" 

print (checkval  in pet);

# () 
# ** 
#+,/,//,%,+,- 

print(10+5+2);
print (20/5+3);
print((10+5)*2);
print(2+3**2);

print( 'B',"A", sep ='*')

# Create a variable age and store the value 22. Print its data type.
age = 22 
print(type("age"));

# Create a variable price = 99.50. Check its data type.
price = 99.50
print(type(price));

# Store your name in a variable and print its data type.
name= 'Simran'
print(type(name));

# Create a variable is_student = True. Check its data type.
is_student = 'true'
print(type(is_student))

# What will be the output? 
# a = 10b = "20"print(type(a))print(type(b))
a = "10" 
b = "20"
print(type(a))
print(type(b));

# Create a list containing 5 numbers and print its type.

# Identify the data types:
#  a = 100b = 10.25c = "Hello"d = Falsee = [1, 2, 3] 
a = 100 
b = 10.25 
c  = "hello"
d = falsee = [1,2,3]; 


# PRINT METHODS 
s = 'hello python wold '; 
newstr= s.strip();
print(s);

print(s.strip().lower());  #methods chaingi
print(s.lower()); 

print(s. title());
print(s. replace("python","java"));
print(s.split(','));
print(s.strip(). find('python'));
print(newstr);
print(newstr.count('z'));
print(newstr.startswith('n'));

print(newstr.endswith('d'));
print(len(newstr));

name,marks="simran","40";
# print (name,marks)
print(f'{name} has scored{marks}');
print('{} scored{}' .format (name,marks));
# print ('%s scored %d'% (namemarks))

# escape charactors
# /n new line 
str = "simran\tgupta"
# print(str)
# immutability 
str1 = "cat";
# str1{0} = "p"
str2 = str1 ;
str1 = "cat1234"
print(str1,str2);

print('python'[1:4]);
print('python'[1:]);
print('school'[::-1]);

str3 = '121'
print(str3==str3[::-1]);

# how we can get input 
marks = int (input("plz enter some thing"));
# print (type( marks));

# control flow 
# age=int(input("pls enter your age:>"))

# if age  >=18:
#     print("you are eligible for vote");
# elif age>=35:
#     print("you are old but eligible")
# else:
#     print("you are nott eligible")

# 90>=A 
# 75>=B 
# 50>=C 
# FAIL 

# let marks 65 
# if marks >=90: 
#     print("A");
# elif marks>=75: 
#     print("B");
# if marks >50: 
#     print("C");
# else: 
#     print("fail");
# ternary opeartor 

status ='pass' if marks >= 40 else 'fail';
print(status)

