# DBTITLE 1, Pandas dataframe
#what is pandas: library for dataset, analyzing, cleaning, exploring & manipulating data, made by Wes Mckinney
#Panda: panel data

#1. quick start
#to install
#pip install pandas
#import
import pandas as pd
#check the version of pandas
pd.__version__

#2. pandas series
#it is like a column in a table, one-D array holding data of any type
pd.Series([1,2,3,4])

#3. labels, if nothing is specified, the values are labeled with their index number, label can be used to access a specified value
#create labels:
a=[1,7,2]
x=pd.Series(a, index=['x','y','z'])
x
#when passing a key/value project, keys will be labels, value will be the series value
calories={'apple':50,'pear':12}
pd.Series(calories)
#you also can select items you want to be in your series
pd.Series(calories, index=['apple'])

#3. data frame, multi-dimensional table
#so series is like a column, a dataframe is many columns that consists a table

#make a dataframe
a={'a':[1,2],'b':[3,2]}
df=pd.DataFrame(a)

#locate row
df.loc[0]#this method returns a series
df.loc[[0,1]]#this method returns a dataframe

#give each row a name
a={'apple':[20,30,40],'pear':[40,50,60]}
df=pd.DataFrame(a, index=['p1','p2','p3'])

#locate the named index
df.loc['p1']

#4. to read a .csv file
df=pd.read_csv('data.csv')
#you can print your df to a string
print(df.to_string())#to_string to print the entire df, if you have a large dataset, pd will only return first nad last 5 rows, so to_string() helps here

#you can check system's max rows to return more data
print(pd.options.display.max_rows)

pd.options.display.max_rows#max row is 60 by default

pd.options.display.max_rows = 600
pd.options.display.max_rows

#big data set are often stored or extracted as JSON, that is a plain text but has the format of an object
#load json file into a datafraem
pd.read_json('data.json')
print(df.to_string())#json is like a string storing python dictionary

#5. analyze dataframes
#view data
df.head(1)#return top 5 rows by default
df.tail(1)#return last 5 rows by default
#info about the dataset
df.info#col_name, non-null count, dtype, memory usage

#6. cleaning data
#bad data could be : empty cells, wrong format, wrong data, duplicates
#you can clean empty cells by removing rows
df.dropna()#by default, it will not change the original dataset, but return a new dataset
#if you wanna change the original dataset
df.dropna(inplace=True)#will not return a new df, but change the original dataset

#replace empy values: 
df.fillna(130, inplace=True)
#for a specific column
df['apple'].fillna(130, inplace=True)
#using mean median mode
df['apple'].fillna(df['calories'].mean(), inplace=True)
#to be noticed that use mode[0], when using mode, because it can be having many modes

#7.convert into a correct format
df['date']=pd.to_datetime(df['date'])
#NaT: not a time, we can remove NaT rows only by
df.dropna(subset=['Date'],inplace=True)#it doesnt work on df['Date'].dropna(inplace=True)

#8. cleaning wrong data
df.loc([7,'duration'])=45#set the 7th row, col duration sets to 45
#removes row ith wrong data
for x in df.index():
  if df.loc[x,'col_name']>10:
    df.drop(x,inplace=True)

#9. duplicates:
#find duplicates
df.duplicated()#it returns True/False table
#remove duplicates
df.drop_duplicates(inplace=True)

#10. pandas corr()
df.corr() #return a matrix
#corr() ignores 'not numeric' columns, >0.6 could be good

#11. plot
df.plot(kind='scatter',x='duration',y='calories')
plot.show()
