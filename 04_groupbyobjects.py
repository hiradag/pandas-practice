import pandas as pd
import numpy as np

delivery= pd.read_csv("deliveries.csv")
imdb=pd.read_csv("imdb-top-1000.csv")
ipl=pd.read_csv("ipl.csv")
movies=pd.read_csv("movies.csv")

#groupby:- It is basically the study of the groups.It applies on categorical col.

genres= imdb.groupby('Genre')

print(genres.sum())


#Q1->FIND THE TOP 3 GENRES BY TOTAL EARNING

print(imdb.groupby('Genre').sum()['Gross'].sort_values(ascending=False).head(3))
#OR below one is better and faster as it is doing sum of gross colu only rather than some of all dataset.
print(imdb.groupby('Genre')['Gross'].sum().sort_values(ascending=False).head(3))

#Q2->Find the genre with highest avg IMDB rating

print(imdb.groupby('Genre')['IMDB_Rating'].mean().sort_values().tail(1))

#Q3->Find director with most popularity:

print(imdb.groupby('Director')['No_of_Votes'].sum().sort_values().tail(1))

#Q4->find number of moviees done by each actor

print(imdb['Star1'].value_counts())
#OR
print(imdb.groupby('Star1')['Series_Title'].count())

#Q5->find total number of groups formed (for e.g. - genre )

print(len(imdb.groupby('Genre')))  #OR
print(imdb['Genre'].nunique())



#csvfilename.grouby('the dsire col we want to group ').size()-->> the o/p will be no. of rows in each group----------------------------------------------------------------


print(imdb.groupby('Genre').size())  #no. of item/rows in each group  OR
print(imdb['Genre'].value_counts())

#the diff. b/w them is size is sorted by index but value_count is sorted by values


print(genres.first())  #prints 1st movie of each group
print(genres.last())  #prints last movie of each group
print(genres.nth(6))  #prints nth movie of each group, here 7th.



#get_group:--------------------------------------------------------------------------

#gives the info. of all the items name of the specified group. fasta and efficient

print(genres.get_group('Horror'))
#or
#FILTERING:
print(imdb[imdb['Genre']=='Fantasy'])

print(genres.groups)  #gives the group names and then the insex position of the items present in it.Dictionary that tracks the record which movie in each group has which index position.

#describe,sample,nunique




#agg method # passing dict:---In pandas, the agg() (aggregate) method can take a dictionary to apply different functions to different columns.This is very useful when using groupby().----------------------------------------------------------


print(genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
))


#agg method # passing list:---In pandas, the agg() method can also take a list to apply multiple functions to the same column.-------------------------------------

print(genres.agg(['min','max']))


#loops on groups:--

#Q> find highest rated movie of each genre.

for group,data in genres:
    print(data[data['IMDB_Rating']==data['IMDB_Rating'].max()])



#split (apply) combine :------------------------------------------

#The data is split into groups based on some column.A function is applied to each group.The results are combined into a final output.

print(genres.apply(min))  #builtin function is inside apply


#Q1-> Find number of movies starting with A for each group

def foo(group):
    return group['Series_Title'].str.startswith('A').sum()
    
print(genres.apply(foo))

#Q2->find ranking of each movie in the group according to IMDB score

def goo(group):
    group['genre_rank']= group['IMDB_Rating'].rank(ascending=False)
    return group

print(genres.apply(goo))


#Q3-> find normalised IMDB rating  group wise

def normal(group):
    group['norm_rating']=(group['IMDB_Rating']- group['IMDB_Rating'].min() )/ (group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
    return group  #purree dataframe ko reconstruct karke wapas dikhata h

genres.apply(normal)





#groupby on multiple cols:----

duo=imdb.groupby(['Director','Star1'])

#size
print(duo.size())
#get_group
print(duo.get_group(('Aamir Khan','Amole Gupte')))  #pass tuple to get info about that specific needed group


#Q->find the most earning actor->director combo
print(duo['Gross'].sum().sort_values(ascending=False).head(1))


#Q->find the best(in-terms of metascore(avg))  actor->genre combo

double=imdb.groupby(['Star1','Genre'])

print(double['Metascore'].mean().sort_values(ascending=False).head(1))






#agg on multiple groupby

print(duo.agg(['min','max'])) 



#Q1->>find the top 10 batsman in terms of runs

runs=delivery.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(runs)

#Q2-> find batsman with max no. of sixes

six=delivery[delivery['batsman_runs']==6]

print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1))

#Q3-->find v kohli's record against all teams

vk= delivery[delivery['batsman']=='V Kohli']

print(vk.groupby('bowling_team')['batsman_runs'].sum())

#Q4-->create a function that can return the highest score of any batsman
def highest(batsman):
  temp_df=delivery[delivery['batsman']== batsman]
  return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

print(highest('MS Dhoni'))
