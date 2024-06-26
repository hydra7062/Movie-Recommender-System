
import streamlit as st
import pickle
import pandas as pd
import requests
def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=156c68a3107d4caf199050e04e7d3137&language=en-US".format(movie_id)
     response  = requests.get(url)
     data =  response.json()
     return "https://images.tmdb.org/t/p/w500/"  + data['poster_path']


def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1 :6]
     recommended_movies = []
     recommended_movies_posters = []

     for i in movies_list:
         # fetch the movie poster
         movie_id = movies.iloc[i[0]].movie_id

         recommended_movies.append(movies.iloc[i[0]].title)

         recommended_movies_posters.append(fetch_poster(movie_id))

     return recommended_movies, recommended_movies_posters




movies_dict  = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.header('Movie Recommender System')


selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values)

if st.button('Show Recommendation'):
     recommended_movie_names ,recommended_movie_posters = recommend(selected_movie_name)
     col1, col2, col3, col4, col5= st.columns(5)    #,col6,col7,col8,col9,col10

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

      st.text("")



     #  with col6:
     #      st.text(recommended_movie_names[5])
     #      st.image(recommended_movie_posters[5])
     #
     #  with col7:
     #      st.text(recommended_movie_names[6])
     #      st.image(recommended_movie_posters[6])
     #
     # with col8:
     #     st.text(recommended_movie_names[7])
     #     st.image(recommended_movie_posters[7])
     #
     # with col9:
     #     st.text(recommended_movie_names[8])
     #     st.image(recommended_movie_posters[8])
     #
     # with col10:
     #     st.text(recommended_movie_names[9])
     #     st.image(recommended_movie_posters[9])









