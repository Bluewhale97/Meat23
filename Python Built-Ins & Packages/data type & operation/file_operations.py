#file operations

#DBTITLE 1, PIP
#package manager for python packages or modules
#package is that conatins all the files you need for a module

#1. to check if PIP installed:
pip --version

#2. download a package
pip intsall pandas

#3. uninstall a package
pip uninstall pack_name #press y for yes

#4. list installed packages
pip list


#DBTITLE 1, try, except, else, finally, raise
try:
  print('hello')
except:
  print('something went wrong')
else: 
  print('nothing went wrong')
finally:
  print("execution was finished")

#to raise an error
try:
  a+1
except:
  raise Exception("sorry, i cannot do it")
else:
  print("nothing went wrong")
finally:
  print('execution was just finished')
  
  
  
#DBTITLE 1, python input, >=3.6 uses input(), 2.7 uses raw_input()
a=input('please input',)
a

#DBTITLE 1, file open
f=open('purchase_seq_test.csv','r')#'r' means the mode is read, there are many modes like 'r','a','w','x', means read, append, write, create respectively
print(f.read())

#open on a different location
#f=open('', 'r')#the path should be absolute path
print(f.read())

#read part of file, first 5 char
f=open('purchase_seq_test.csv','r')
print(f.read())

#read one line
f.readline()

# read line by line
for x in f:
  print(x)


# how to write to existing file
f=open('purchase_seq_train.csv','w')#use append mode or 'w' write mode
f.write('12dj32ughdshfeseewfpw392370934270973207320')

# create a file, use 'w' mode
f=open('a.csv','x')
f.write('yes i like it')


#delete a file
import os
#os.remove('a.csv')

#check if file exists before delete, if not, cease to operate
if os.path.exists('a.csv'):
  os.remove('a.csv')
  
  
#delete entire folder
os.rmdir()



