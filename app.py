import streamlit as st
import pickle as pkl
import pandas as pd
import requests

def fetchImageUrl(movie_id):

    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=b89a59fc22b4010ac1444f7509e70a88&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500"+ data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movieListNames = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended = []
    posterList = []
    for i in movieListNames:
        movieID = movies.iloc[i[0]].movie_id
        posterList.append(fetchImageUrl(movieID))
        recommended.append(movies.iloc[i[0]].title)
    return recommended, posterList

movies_list = pkl.load(open('movies_dict.pkl','rb'))
movies_list_values = movies_list['title'].values
movies = pd.DataFrame(movies_list)
similarity = pkl.load(open('similarity.pkl', 'rb'))
st.title("Movie Recommender System")

selected_option_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button('Recommend'):
    recomendationMovies, moviePosters = recommend(selected_option_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recomendationMovies[0])
        st.image(moviePosters[0])

    with col2:
        st.text(recomendationMovies[1])
        st.image(moviePosters[1])
    with col3:
        st.text(recomendationMovies[2])
        st.image(moviePosters[2])
    with col4:
        st.text(recomendationMovies[3])
        st.image(moviePosters[3])
    with col5:
        st.text(recomendationMovies[4])
        st.image(moviePosters[4])





