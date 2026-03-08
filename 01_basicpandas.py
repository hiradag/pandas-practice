import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#PANDAS:Pandas is a Python library used for data analysis and data manipulation. It helps us work with structured data like tables.

#LISTS:-A list is a data structure in Python used to store multiple values in a single variable. Lists are ordered, changeable (mutable), and allow duplicate values.

#Creating a Pandas Series from a List--------------------------------------------------------------

country=['india','lio','japan','nepal'] #string
print(pd.Series(country))

runs=[13,24,30,32]#integers
print(pd.Series(runs))

#creating a pandas series by custom index AND setting a name
marks=[67,75,78,90,98]
subjects=['maths','english','science','sst','cs']
print(pd.Series(marks,index=subjects,name='Nitish marks'))
#---------------------------------------------------------------------------------------------------

#Creating a Pandas Series from a Dictionary----------------------------------------------------------

marks={ 'maths':67,'english':89,'science':98,'hindi':88}
print(pd.Series(marks))




#Creating Series using read_csv

df = pd.read_csv("movies.csv")
print(df)    #GIVES O/P IN DATAFRAME FORM

ds= pd.read_csv("movies.csv")
print(ds.squeeze())#In Pandas, (squeeze=True) only works when there is exactly ONE column in the file.If the CSV file has 2 or more columns, pandas cannot convert it to a Series, so it keeps it as a DataFrame

print(pd.read_csv("movies.csv",index_col="imdb_id"))   #imdb_id becomes index




#HEAD AND TAIL:--- Head shows first 5 rows by default and Tail shows bottom 5 rows by default.-------------------------------------------

print(df.head())  #prints first 5 rows . (df = pd.read_csv("movies.csv"))
print(df.head(3))  #we can modify it by entering i/p from our side.

print(df.tail())   #prints last 5 rows . (df = pd.read_csv("movies.csv"))
print(df.tail(2))   #we can modify it by entering i/p from our side.


#SAMPLE:- by deafault gives one random row in o/p
print(df.sample())   # 1 random row
print(df.sample(7))  # 7 random rows

#VALUE_COUNTS: value_counts() is used to count how many times each unique value appears in a column or Series.
print(df["year_of_release"].value_counts())
print(df["actors"].value_counts())


#Sort_values:-
print(df.sort_values("imdb_rating",ascending=False))


#Sort_index():-sort_index() is used to sort a Series or DataFrame based on the index (row labels).
print(df.sort_index())


#SERIES MATHS METHOD


#COUNT= DOES NOT COUNT MISSING VALUES  BUT SIZE COUNTS MISSING VALUES

#COUNT:- count() is used to count the number of non-missing values (not NaN) in a Series or DataFrame.

print(df["imdb_rating"].count())  #Count how many movies have IMDb rating
print(df["title_x"].count())    #Count how many movie titles exist

dv = pd.read_csv("vk.csv")
print(dv) 
print(dv.count())

#SUM AND PRODUCT:------

print(dv.sum())

print(dv.max())
print(dv.min())
print(dv.describe())  #SHOWS MEAN STD MIN AND OTHER INFO IN O/P


#SERIES INDEXING

#integer indexing

x=pd.Series([12,13,14,79,9])
print(x[0])
print(x[1])

#Negative Indexing: NOT WORK IN SERIES

print(dv[dv["match_no"]==100])   #details of match no. 100


#SLICING:--

print(dv[5:16])  #vk runs from 6 to 15 match no
print(dv[-5:])    #vk runs in last 5 matches   #NEGATIVE SLICING

#FANCY INDEXING:--

print(dv.iloc[[1,3,5,7]])


#The reason slicing works but fancy indexing fails is because of how pandas treats DataFrame slicing vs list indexing.5:16 is a slice. In a DataFrame, slicing like this means row slicing.Here [1,3,5,7] is a list, not a slice.For a DataFrame, pandas interprets this as:Select columns named 1,3,5,7.




dv.plot()
plt.show()
