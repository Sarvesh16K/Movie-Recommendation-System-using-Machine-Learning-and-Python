import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
movies= pd.read_csv("imdb_top_1000.csv")
movies2 = movies.fillna(method="pad")
df= movies.fillna({"Certificate":"UA", "Meta_score":60, "Gross":25000000})
columns=["Series_Title","Released_Year","Genre","IMDB_Rating","Meta_score","Director","Star1","Star2","Star3","Star4"]
def index(x):
    rank=[]
    for k in range(0, x.shape[0]):
        rank.append(k)
    return rank
df["Rank"] = index(df)
df["Movie_id"] = index(df)
def get_imp_feat(data):
    impfeat=[]
    for i in range(0, data.shape[0]):
        impfeat.append(data["Series_Title"][i]+" "+data["Released_Year"][i]+" "+data["Genre"][i]+" "+str(data["IMDB_Rating"][i])+" "+data["Director"][i])
    return impfeat
df["Imp_Features"] = get_imp_feat(df)
cm = CountVectorizer().fit_transform(df["Imp_Features"])
cs = cosine_similarity(cm)
title= input("Enter your favorite movie: ")
movie_rat = df[df.Series_Title == title]["Movie_id"].values[0]
scores = list(enumerate(cs[movie_rat]))
sorted_scores = sorted(scores, key = lambda x:x[1], reverse = True)
sorted_scores = sorted_scores[1:]
j=0
print(f"Recommendations for movie {title}: ")
for item in sorted_scores:
    movie_rat = df[df.Movie_id == item[0]]["Series_Title"].values[0]
    print(j+1, movie_rat)
    j = j + 1
    if j>9:
        break

