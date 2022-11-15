import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
movies= pd.read_csv("imdb_top_1000.csv")
movies2 = movies.fillna(method="pad")
df= movies.fillna({"Certificate":"UA", "Meta_score":60, "Gross":25000000})
columns=["Series_Title","Released_Year","Genre","IMDB_Rating","Meta_score","Director","Star1","Star2","Star3","Star4"]
df["Released_Year"].replace("PG","1995",inplace=True)
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
def get_actors(data1):
    actor=[]
    for a in range(0, data1.shape[0]):
        actor.append(data1["Star1"][a]+" , "+data1["Star2"][a]+" , "+data1["Star3"][a]+" , "+data1["Star4"][a])
    return actor
df["Actors"] = get_actors(df)
pop = []
result = []
result1 = []
result2 = []
for p in range(0, 999):
    pop.append(df["Series_Title"][p])
print("Top 10 most popular movies of all time:")
x=0
for elel in pop:
    print(x+1, elel)
    x = x+1
    if x>9:
        break
gen= input("Enter your favorite Genre: ")
for k in range(0, 999):
    m = list(map(str, df["Genre"][k].split(", ")))
    for n in m:
        if (gen == n):
            result.append(df["Series_Title"][k])
    m.clear()
fav_act = input("Enter your favorite actor: ")
for l in range(0, 999):
    r = list(map(str, df["Actors"][l].split(" , ")))
    for t in r:
        if(fav_act == t):
            result1.append(df["Series_Title"][l])
    r.clear()
age = input("Enter your age(1-100):")
if int(age)<1 or int(age)>100:
    print("Invalid age. Please re-enter your correct age.")
elif int(age)<=15:
    for y in range(0, 999):
        mn = list(map(str, df["Genre"][y].split(", ")))
        for a in mn:
            if (a == "Animation"):
                result2.append(df["Series_Title"][y])
    mn.clear()
elif int(age)>15 and int(age)<30:
    for u in range(0, 999):
        un = list(map(str, df["Released_Year"][u]))
        str1=""
        for r in un:
            str1 = str1 + r
            if int(str1)>1999:
                result2.append(df["Series_Title"][u])
    un.clear()
else:
    for d in range(0, 999):
        dn = list(map(str, df["Released_Year"][d]))
        str2=""
        for v in dn:
            str2 = str2 + v
            if int(str2)<2000 and int(str2)>1000:
                result2.append(df["Series_Title"][d])
    dn.clear()
print(" ")
print(f"Top 10 {gen} Movies: ")
q=0
for genre in result:
    print(q+1, genre)
    q = q+1
    if q>9:
        break
print(" ")
print(f"Top 10 Movies of {fav_act}: ")
w=0
for fav in result1:
    print(w+1, fav)
    w = w+1
    if w>9:
        break
print(" ")
print("Popular movies for your age group are:")
s=0
for agegrp in result2:
    print(s+1, agegrp)
    s = s+1
    if s>9:
        break