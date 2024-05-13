import math
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import quote


def prepare_data(x):
    return str.lower(x.replace(" ", ""))


def create_soup(x):
    return x["Genre"] + " " + x["Tags"] + " " + x["Actors"] + " " + x["ViewerRating"]


def get_recommendations(title, cosine_sim):
    global result
    title = title.replace(" ", "").lower()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:51]
    movie_indices = [i[0] for i in sim_scores]
    result = netflix_data.iloc[movie_indices]
    result.reset_index(inplace=True)
    return result


netflix_data = pd.read_csv(
    "app/NetflixDataset.csv", encoding="latin-1", index_col="Title"
)
netflix_data.index = netflix_data.index.str.title()
netflix_data = netflix_data[~netflix_data.index.duplicated()]
netflix_data.rename(columns={"View Rating": "ViewerRating"}, inplace=True)
Language = netflix_data.Languages.str.get_dummies(",")
Lang = Language.columns.str.strip().values.tolist()
Lang = set(Lang)
Titles = set(netflix_data.index.to_list())

netflix_data["Genre"] = netflix_data["Genre"].astype("str")
netflix_data["Tags"] = netflix_data["Tags"].astype("str")
netflix_data["IMDb Score"] = netflix_data["IMDb Score"].apply(
    lambda x: 6.6 if math.isnan(x) else x
)
netflix_data["Actors"] = netflix_data["Actors"].astype("str")
netflix_data["ViewerRating"] = netflix_data["ViewerRating"].astype("str")
new_features = ["Genre", "Tags", "Actors", "ViewerRating"]
selected_data = netflix_data[new_features]
for new_feature in new_features:
    selected_data.loc[:, new_feature] = selected_data.loc[:, new_feature].apply(
        prepare_data
    )
selected_data.index = selected_data.index.str.lower()
selected_data.index = selected_data.index.str.replace(" ", "")
selected_data["soup"] = selected_data.apply(create_soup, axis=1)

count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(selected_data["soup"])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
selected_data.reset_index(inplace=True)
indices = pd.Series(selected_data.index, index=selected_data["Title"])
result = 0
df = pd.DataFrame()


def movie_details(name):
    global df
    details_list = df[df["Title"] == name].to_numpy().tolist()
    if not details_list:
        return "Not found"
    return details_list
