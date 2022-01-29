from apyori import apriori
from asyncio.windows_events import NULL
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ratings_df = pd.read_csv('backend/MachineLearningModel/ratings_small.csv')
# contains the ratings of the movies given by a user with userid
movies_df = pd.read_csv('backend/MachineLearningModel/movies_metadata.csv')
# contains the information about each movie

# print(ratings_df.head())
# print(movies_df.head())

# this removes the rows in the movies dataset which have no title
title_mask = movies_df['title'].isna()
movies_df = movies_df.loc[title_mask == False]

movies_df = movies_df.astype({'id': 'int64'})
df = pd.merge(
    ratings_df, movies_df[['id', 'title']], left_on='movieId', right_on='id')
df.drop(['timestamp', 'id'], axis=1, inplace=True)
df = df.drop_duplicates(['userId', 'title'])
df_pivot = df.pivot(index='userId', columns='title', values='rating').fillna(0)
df_pivot = df_pivot.astype('int64')


def encode_ratings(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1


df_pivot = df_pivot.applymap(encode_ratings)
newDf = df_pivot.values.tolist()
columnsList = df_pivot.columns.values.tolist()

for i in range(0, len(df_pivot.index)):
    for j in range(0, len(df_pivot.columns)):
        if newDf[i][j] != 0:
            newDf[i][j] = columnsList[j]
        else:
            newDf[i][j] = NULL

finalDf = []
for i in range(0, len(newDf)):
    temp = []
    for j in range(0, len(newDf[i])):
        if newDf[i][j] != NULL:
            temp.append(str(newDf[i][j]))
    if len(temp) > 0:
        finalDf.append(temp)

rules = apriori(transactions=finalDf, min_support=0.03,
                min_confidence=0.2, min_lift=3, min_length=2, max_length=2)
results = list(rules)


def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, lifts))


tempArr = inspect(results)


def Sort_Tuple(tup):
    tup.sort(key=lambda x: x[2])
    return tup


tempArrSorted = Sort_Tuple(tempArr)
tempArrSorted.reverse()


def getResults(movie, limit):
    res = []
    ct = 0
    for i in tempArrSorted:
        if(i[0] == movie):
            res.append(i)
            ct += 1
        if(ct == limit):
            break
    return res


print(getResults('Rocky III', 5))
