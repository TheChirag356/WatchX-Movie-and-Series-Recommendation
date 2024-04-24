![WatchX Banner](/app/static/img/watchX.svg)
<hr>
<p><font size="3">
This Movie Recommender System is a web application designed to deliver personalized suggestions for films and television shows based on your specific likes. The app recommends a list of media according to the list of entered choices of movies/series in your preferred language.
</p>

 # This web-app contains 3 main pages:
- [Home Page](#home-page)
- [Recommendation Page](#recommendation-page)
- [Movie Detail Page](#movie-detail-page)


## Home Page

Here, users can select a list of their favourite movies and series along with their preferred language. For instance, user want to choose two horror movies (like "Insidious" and "Insidious Chapter 2"), an action series (such as "Supergirl"), and a drama series (like "Suits"), and specify English and Hindi as per their preferred languages. Upon clicking the "Get Started" button, users will be presented with a list of personalized recommendations.
![](/app/static/screenshots/Screenshot-HomePage.png)

## Recommendation Page
Here, users will receive poster images of all the recommended movies and series, sorted based on their IMDb scores.
![](/app/static/screenshots/Screenshot-RecommendationPage1.png)
![](/app/static/screenshots/Screenshot-RecommendationPage2.png)

Clicking on any poster image will redirect the user to the Movie Details page for the corresponding title.

## Movie/Series Detail Page
Here are the complete details of the user-selected title, including genre, movie/series summary, languages in which the movie/series is available, IMDb scores, directors, writers, actors, and more. Users will also find a link at the end of the page to the Netflix page of the corresponding title. 
![](/app/static/screenshots/Screenshot-MovieDetailPage1.png)

# Features

- **Personalized Recommendations:** Utilizes machine learning algorithms to generate personalized recommendations based on user preferences.
  
- **User Input:** Users can input a list of their favorite movies, and the system will recommend similar movies available on Netflix.
  
- **Netflix Integration:** Recommends movies available on Netflix, leveraging its extensive collection of titles.
  
- **Python and Flask:** Built using Python programming language and Flask web framework for backend development.
  
# Future Upgrades
- **Real-Time Updates:** Implement a mechanism to fetch real-time data from Netflix's API or other streaming platforms to ensure that the recommendations are always up-to-date with the latest releases and user ratings.

- **Sentiment Analysis:** Integrate sentiment analysis techniques to analyze user reviews and feedback on movies, providing insights into the emotional response to each recommendation and enhancing the recommendation algorithm.

- **Sentiment Analysis:** Integrate sentiment analysis techniques to analyze user reviews and feedback on movies, providing insights into the emotional response to each recommendation and enhancing the recommendation algorithm.

- **Localized Recommendations:** Customize recommendations based on the user's location or language preferences, taking into account regional content availability and cultural differences in movie preferences.

-  **Integration with Other Streaming Platforms:** Extend the system to recommend movies from other streaming platforms such as Amazon Prime Video, Disney Hotstar etc.


# How To Use

To be able to use this web app locally in a development environment you will need the following:

1) You will need [Git](https://git-scm.com) installed on your computer.

2) Then From your terminal, you should do the following:

```cmd
# Clone this repository
git clone https://github.com/TheChirag356/WatchX-Movie-and-Series-Recommendation

# Go into the repository
cd Movie-Recommendation

# Install all  (if you already haven't)
pip install -r requirements.txt

```
3) To run this application you don't need to have any special configuration but make sure you don't change the directory of the project otherwise you can recieve errors while you try to run the app.

4) You can run the Netflix React App using the following command from your terminal:

```bash
# Run the app
python app.py
```

# Team
Anushka([@anushka](https://github.com/anushka-mazumdar))

Chirag Arora([@chiragarora](https://github.com/TheChirag356)) 

Himanshi Gupta([@himanshigupta](https://github.com/Himanshigupta1624))

Krishan Mittal([@krishanmittal](https://github.com/Krishan098))



# Show Your Support 

Give a ⭐️ if you like this project!
