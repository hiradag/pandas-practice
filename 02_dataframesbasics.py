import numpy as np
import pandas as pd

#CREATING DATAFRAMES:-  using lists, using dictionary , using read_csv.

#using lists:-------
student_data=[[100,80,10],[90,70,7],[120,100,14],[80,50,2]]
print(pd.DataFrame(student_data,columns=['iq','marks','package']))

#using dictionary:-------------
student_dict={ 'iq':[100,90,120,80],'marks':[80,70,100,50],'package':[10,7,14,2]}
print(pd.DataFrame(student_dict))

#DataFrame Attribute and Methods:--------------


movies= pd.read_csv("movies.csv")
ipl=pd.read_csv("ipl.csv")


#shape:--
print(movies.shape)  #o/p:-  data of 1629 movies divided into 18 columns
print(ipl.shape)  #total matches is 950 


#dtypes:---  Each column's datatype
print(movies.dtypes)
print(ipl.dtypes)


#index:-- we can fetch index range
print(movies.index)
print(ipl.index)

#columns:-- fetches the name of all columns
print(movies.columns)
print(ipl.columns)

#values: -- It converts pandas data into a NumPy array
print(ipl.values)
print(movies.values)

#head and tail:---- by default gives top 5 rows and botto 5 rows respectively.

print(ipl.head())
print(ipl.tail())
print(ipl.sample(6))  #GIVES RANDOMLY ANY 6 ROWS


#info():-In pandas, the .info() function is used to get a quick summary of a DataFrame.

print(ipl.info())
print(movies.info)


#describe():--In pandas, the .describe() function is used to get statistical summary of numerical columns in a DataFrame or Series.---------------
print(movies.describe())
print(ipl.describe)

#isnull: checks whether a missing value is there or not in a column-----------------------
print(ipl.isnull())
print(ipl.isnull().sum()) #each col has how many missing values

#duplicates(): checks whether a row is duplicated or not---------------------
print(ipl.duplicated().sum())  #total no. of duplicated rows

#rename:--- changes the name of the column

print(ipl.rename(columns={'Season':'Year'}))  #Season cahnges to Year


#We can select row or columns or both from a DataFrame:--


#Selecting columns from a DataFrame:-----------------------------------------------

#single column:
print(ipl['Venue'])
print(movies['imdb_rating'])

#multiple columns:
print(ipl[['ID','City','Season']])


#Selecting rows from a DataFrame:--------------

#TWO METHODS:  iloc(searches using index position) and loc(searches using index labels)

#single row:--------
print(movies.iloc[0])  #returns the details of movie which is index 0. {Here 0 is the index position .}
print(movies.loc[0])  #{Here 0 is the index label}

#multiple rows:------
print(movies.iloc[0:5])  #returns the details of movie from index 0 to 4

#Fancy indexing:------
print(movies.iloc[[0,4,5]])  #returns the details of movie which is on index 0 ,4 and 5


#SELECTING BOTH ROW AND COLUMNS:-----------------------------------------------------
print(movies.iloc[0:3,0:3])






#FILTERING A DATAFRAME:

#Q1--->  find all final winners

# print(ipl[ipl['MatchNumber']=='Final'])
# df=ipl[ipl['MatchNumber']=='Final']

# print(df[['Season','WinningTeam']])  OR
print(ipl[ipl['MatchNumber']=='Final'][['Season','WinningTeam']])

#Q2--> how many super over finishes have occured

print(ipl[ipl['SuperOver']=='Y'].shape[0])


#Q3--->how many matches has csk won in kolkata

df=ipl[ipl['City']=='Kolkata']
print(df[df['WinningTeam']=='Chennai Super Kings'].shape) 
#OR
print(ipl[(ipl['City']=='Kolkata') & (ipl['WinningTeam']=='Chennai Super Kings')].shape)


#Q4--->toss winner is match winner in percentage:

print(ipl[ipl['TossWinner']==ipl['WinningTeam']].shape[0]/ipl.shape[0])


#Q5--->movies with rating higher than 8 and votes>1000:

print(movies[(movies['imdb_rating']>8) & (movies['imdb_votes']>1000)].shape[0])