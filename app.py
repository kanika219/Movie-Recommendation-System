import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title) 
        recommended_movies_posters. append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies = pickle.load(open("movie_list.pkl",'rb'))
similarity = pickle.load(open("similarity.pkl",'rb'))
movies_list = movies['title'].values

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies_list
)

if st.button("Recommend"):
    name,posters = recommend(selected_movie_name)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(name[0])
        st.image(posters[0])
    with col2:
        st.text(name[1])
        st.image(posters[1])
    with col3:
        st.text(name[2])
        st.image(posters[2])
    with col4:
        st.text(name[3])
        st.image(posters[3])
    with col5:
        st.text(name[4])
        st.image(posters[4])

