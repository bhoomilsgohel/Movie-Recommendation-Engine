import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ratings_df = pd.read_csv('backend/MachineLearningModel/ratings_small.csv')
movies_df = pd.read_csv('backend/MachineLearningModel/movies_metadata.csv')

ratings_df.head()
ratings_df.info()
movies_df.head()
movies_df.info()

plt.figure(figsize=(10,5))
ax = sns.countplot(data=ratings_df, x='rating')
labels = (ratings_df['rating'].value_counts().sort_index())
plt.title('Distribution of Ratings')
plt.xlabel('Ratings')

for i,v in enumerate(labels):
    ax.text(i, v+100, str(v), horizontalalignment='center', size=14, color='black')
plt.show()

title_mask = movies_df['title'].isna()
movies_df = movies_df.loc[title_mask == False]

movies_df = movies_df.astype({'id': 'int64'})

df = pd.merge(ratings_df, movies_df[['id', 'title']], left_on='movieId', right_on='id')
df.head()
df.drop(['timestamp', 'id'], axis=1, inplace=True)

df = df.drop_duplicates(['userId','title'])
df_pivot = df.pivot(index='userId', columns='title', values='rating').fillna(0)

df_pivot = df_pivot.astype('int64')

def encode_ratings(x):
    if x<=0:
        return 0
    if x>=1:
        return 1

df_pivot = df_pivot.applymap(encode_ratings)

df_pivot.head()

from mlxtend.frequent_patterns import apriori

frequent_itemset = apriori(df_pivot, min_support=0.07, use_colnames=True)

frequent_itemset.head()

from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemset, metric="lift", min_threshold=1)
rules.head()

df_res = rules.sort_values(by=['lift'], ascending=False)
df_res.head()

df_MIB = df_res[df_res['antecedents'].apply(lambda x: len(x) ==1 and next(iter(x)) == 'Men in Black II')]

df_MIB = df_MIB[df_MIB['lift'] > 2]
df_MIB.head()

movies = df_MIB['consequents'].values

movie_list = []
for movie in movies:
    for title in movie:
        if title not in movie_list:
            movie_list.append(title)
movie_list[0:10]