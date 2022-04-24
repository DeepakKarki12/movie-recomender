import pandas as pd
import pickle
import requests
import streamlit as st

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ec6260e66f6bd35bd1516b8242a1d984&language=en-US'.format(movie_id))
#     data = response.json()
#     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
#
#
# st.title("movie recomendor system")
# similarity = pickle.load(open("similarity.pkl","rb"))
# movie_list = pickle.load(open("movie.pkl","rb"))
# new_df  = pd.DataFrame(movie_list)
# movie_name = st.selectbox('search here',new_df['title'].values)
#
#
# def recommend(movie):
#     mov_index = new_df[new_df['title']==movie].index[0]
#     distance = similarity[mov_index]
#     movie_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x:x[1])[1:6]
#     rec_movie = []
#     rec_poster = []
#     for i in movie_list:
#         rec_movie.append(new_df.iloc[i[0]].title)
#         rec_poster.append(fetch_poster(new_df.iloc[i[0]].movie_id))
#     return rec_movie,rec_poster
# if st.button('recommend'):
#     movie_names,poster = recommend(movie_name)
#     col1, col2, col3, col4, col5 = st.columns(5)
#
#     with col1:
#         st.text(movie_names[0])
#         st.image(poster[0])
#
#     with col2:
#         st.text(movie_names[1])
#         st.image(poster[1])
#     with col3:#
#         st.text(movie_names[2])
#         st.image(poster[2])
#     with col4:
#         st.text(movie_names[3])
#         st.image(poster[3])
#     with col5:
#         st.text(movie_names[4])
#         st.image(poster[4])
#
# ########################################################################################################################
def recommned_movies(mov_name):

    movie_index = movie[movie['title']==mov_name].index[0]
    movie_no= sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x: x[1])[1:6]
    name=[]
    posters= []

    for i in movie_no :
        name.append(movie.iloc[i[0]].title)
        response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=ec6260e66f6bd35bd1516b8242a1d984&language=en-US".format(movie.iloc[i[0]].movie_id))
        poster = response.json()['poster_path']
        posters.append("https://image.tmdb.org/t/p/w500"+poster)


    return posters,name
st.title("Movie Recomender")
mov = pickle.load(open('movie.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movie = pd.DataFrame(mov)
selected_movie=st.selectbox("search here",movie['title'].values)

if st.button("remcommend"):
    poster,name = recommned_movies(selected_movie)
    col1, col2, col3 ,col4 ,col5 = st.columns(5)

    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])

    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])





