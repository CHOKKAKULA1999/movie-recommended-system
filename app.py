import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    """_summary_

    Args:
        movie_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    print("-------------------------------------")
    url         = "https://api.themoviedb.org/3/movie/{}?api_key=f894220560ada36c4c4afb8a1a5a845a&language=en-US".format(movie_id)
    print(url)
    response    = requests.get(url)
    data        = response.json()
    print(data)
    poster_path = data["poster_path"]
    
    full_path   = "https://image.tmdb.org/t/p/w500" + poster_path
    print(full_path)
    return full_path 

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])) , reverse = True ,key = lambda x:x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        
        #recommend_movies.append(movies.iloc[i[0]].title)
        #fetch poster from API
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names,recommended_movie_posters        

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("MOVIE-RECOMMENDER-SYSTEM-[SUNDAR]")
movie_list = movies["title"].values



selected_movie = st.selectbox('type or select a movie from the dropdown',
movie_list)

if st.button('SHOW-RECOMMEND'):
    recommended_movie_names , recommended_movie_posters = recommend(selected_movie)
    names,posters = recommend(selected_movie)
    
    col1 , col2, col3 , col4 ,col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])