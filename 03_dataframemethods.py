import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
ipl=pd.read_csv("ipl.csv")
movies=pd.read_csv("movies.csv")
batsman=pd.read_csv("batsman_runs_ipl.csv")


#value_counts(series and dataframe):- frequency counts-----------------------------------------------------------------------------------------------------------------------------

a=pd.Series([1,1,1,2,2,3])
print(a.value_counts())  #IN SERIES

marks= pd.DataFrame([[100,80,10],[90,70,7],[120,100,14],[80,70,14],[80,70,14]],columns=['iq','marks','package'])

print(marks.value_counts())  #GIVE HOW MANY ROWS HAS REPEATED

#Q1-> find which player has won most potm -> in finals and qualifiers

df=ipl[(ipl['MatchNumber']== 'Final') | (ipl['MatchNumber']== 'Qualifier 1') | (ipl['MatchNumber']=='Qualifier 2')]

dm=df['Player_of_Match'].value_counts()
print(dm.head(1))

#Q2-> Toss decision plot

#ipl['TossDecision'].value_counts().plot(kind='bar')
#plt.title("Toss Decision Distribution")
#plt.xlabel("Decision")
#plt.ylabel("Count")

#plt.show()

#Q3->how many matches each team has played
print(ipl['Team1'].value_counts() + ipl['Team2'].value_counts())


#sort_values(series and DataFrame):-------------------------------------------------------------------------------------------------

x= pd.Series([12,14,1,5,8])
print(x.sort_values())  #sorting in series


#sorting on basis of 1 col:--
print(movies.sort_values('title_x')) #sorting the movies dataframe , 1st number then alphabet a,b......


#property of sort_value() is that it sends all the missing and nan values at the last by default. if we want to give nan beginning position , then use (na_position='first')

#sorting on basis of multiple col:--

print(movies.sort_values(['year_of_release','title_x'])) #at first sorting on the basis of year , then on the basis of alphabets or digits



#rank(series):----------------------------------------------------------------------

print(batsman['batsman_run'].rank(ascending=False)) 

batsman['batting_rank']= batsman['batsman_run'].rank(ascending=False)  #creating a new col named batting_rank in batsman dataframe

print(batsman.sort_values('batting_rank'))


#sort index(series and dataframe):-------------------------------------------------------------------------

print(movies.sort_index(ascending=False))  #here we are using ascending=false , as the index in movies dataset is already sorted in ascending order


#set index(datframe):------------------------------------

print(batsman.set_index('batter'))  #index is now batter name


#reset index(series and dataframe):-----------------------

print(batsman.reset_index())  #reset the changes made through set index


#if we want to make batting rank as index , then if we use(set_index('batting rank'),then there will be a problem that the batter column will be lost.To overcome this we use:-)

print(batsman.reset_index().set_index('batting_rank'))#how to replace existing index w/o loosing 

#reset index in Series:---
marks={ 'maths':64 , 'english':90,'Math':79,'sst':89}
marks_series=pd.Series(marks)
print(marks_series.reset_index())  #SERIES CONVERTED TO DATAFRAME *******************



#rename(dataframe)->index:--------------------col ko rename , by default: index ko no rename
print(movies.rename(columns={'title_x':'title','actors':'hero'}))

# #if we want to rename index
# movies.set_index('title_x',inplace=True)
# print(movies.rename(index={'Uri: The Surgical Strike':'Uri','Battalion 609':'Battalion'}))


#unique(series):--------------------------------------------------------------------
temp=pd.Series([1,1,2,2,3,3,5,6,np.nan,6,np.nan,np.nan])
print(temp.unique())
print(ipl['Season'].unique()) #pick up unique value from a column

#nunique: counts no. of unique values . excluding nan
#if we use len(variable.unique()): then it will count the nan also



#isnull/notnull  (series+dataframe)--------------------------------------------------

#isnull()(checks each value that it is null or not , if null then it will give True and if not null then it will give False)
print(temp.isnull())

#notnull()(opposite of isnull)
print(temp.notnull())


#hasnans(Series)(checks whether there is atleast any one missing value is present or not)
print(temp.hasnans)


#dropna()(series+dataframe)-----------------
print(temp.dropna())
#if there is any one missing value in the row,then it will remove the whole row.
#if we want to remove only that row where all values are missing then (temp.dropna(how='all')) for dataframe

#fillna(series+dataframe)-------------------

print(temp.fillna('unknown'))


#drop_duplicates()(series+dataframe):------

print(temp.drop_duplicates())


#Q-> last match played by V kohli in Delhi date
dv = ipl[
    ((ipl['Team1Players'].str.contains('V Kohli')) |
     (ipl['Team2Players'].str.contains('V Kohli'))) &
     (ipl['City'] == 'Delhi')
]
print(dv['Date'].max())

#drop(series+dataframe):---------------------------------------------------------

print(temp.drop(index=[0,6]))
print(movies.drop(columns=['title_x','imdb_id'])) #droping col from dataframe
print(movies.drop(index=[0,2])) #droping rows from dataframe


#apply(series+dataframe):---------------------------------------------------

def sigmoid(value):
    return 1/1+np.exp(-value)

print(temp.apply(sigmoid))   # in series


points_df=pd.DataFrame(
    {
        '1st point':[(3,4),(-6,5),(0,0),(-10,1),(4,5)],
        '2nd point':[(-3,4),(0,0),(2,2),(10,10),(1,1)]
    }
)
print(points_df)


def euclidean(row):
    pt_A=row['1st point']
    pt_B=row['2nd point']

    return((pt_A[0] - pt_B[1])**2 + (pt_A[1]-pt_B[1])**2)**0.5

print(points_df.apply(euclidean,axis=1))




