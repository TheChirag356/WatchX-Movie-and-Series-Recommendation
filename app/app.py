import math
from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_wtf import FlaskForm

def prepare_data(x):
        return str.lower(x.replace(" ", ""))

def create_soup(x):
    return x['Genre'] + ' ' + x['Tags'] + ' ' +x['Actors']+' '+ x['ViewerRating']

def get_recommendations(title, cosine_sim):
    global result
    title=title.replace(' ','').lower()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:51]
    movie_indices = [i[0] for i in sim_scores]
    result =  model_data.iloc[movie_indices]
    result.reset_index(inplace = True)
    return result

model_data = pd.read_csv('Dataset.csv',encoding='latin-1', index_col = 'Title')
model_data.index = model_data.index.str.title()
model_data = model_data[~model_data.index.duplicated()]
model_data.rename(columns={'View Rating':'ViewerRating'}, inplace=True)
Language = model_data.Languages.str.get_dummies(',')
Lang = Language.columns.str.strip().values.tolist()
Lang = set(Lang)
Titles = set(model_data.index.to_list())

model_data['Genre'] = model_data['Genre'].astype('str')
model_data['Tags'] = model_data['Tags'].astype('str')
model_data['IMDb Score'] = model_data['IMDb Score'].apply(lambda x: 6.6 if math.isnan(x) else x)
model_data['Actors'] = model_data['Actors'].astype('str')
model_data['ViewerRating'] = model_data['ViewerRating'].astype('str')
new_features = ['Genre', 'Tags', 'Actors', 'ViewerRating']
selected_data = model_data[new_features]
for new_feature in new_features:
    selected_data.loc[:, new_feature] = selected_data.loc[:, new_feature].apply(prepare_data)
selected_data.index = selected_data.index.str.lower()
selected_data.index = selected_data.index.str.replace(" ",'')
selected_data['soup'] = selected_data.apply(create_soup, axis = 1)

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(selected_data['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
selected_data.reset_index(inplace = True)
indices = pd.Series(selected_data.index, index=selected_data['Title'])
result = 0
df = pd.DataFrame()

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', languages = Lang, titles = Titles) 

@app.route('/about', methods=['POST'])
def getvalue():
    global df
    movienames = request.form.getlist('titles')
    languages = request.form.getlist('languages')
    for moviename in movienames:
        get_recommendations(moviename,cosine_sim2)
        for language in languages:
            df = pd.concat([result[result['Languages'].str.count(language) > 0], df], ignore_index=True)
    df.drop_duplicates(keep = 'first', inplace = True)
    df.sort_values(by = 'IMDb Score', ascending = False, inplace = True)
    images = df['Image'].tolist()
    titles = df['Title'].tolist()
    return render_template('result.html',  titles =  titles, images = images)

@app.route('/moviepage/<name>')
def movie_details(name):
    global df
    details_list = df[df['Title'] == name].to_numpy().tolist()
    return render_template('moviepage.html', details = details_list[0])


if __name__ == '__main__':
    app.config["SECRET_KEY"]="thisisasecretkey"
    app.run(debug=True)
