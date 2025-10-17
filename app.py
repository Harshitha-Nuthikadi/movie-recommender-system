import pickle
import streamlit as st
import requests
import pandas as pd


# --- Function to fetch movie poster from TMDB ---
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if response failed
        data = response.json()

        # Check if poster exists
        if 'poster_path' in data and data['poster_path']:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            # Nice placeholder image
            return "https://via.placeholder.com/300x450?text=No+Poster"
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/300x450?text=Error+Loading+Poster"


# --- Function to recommend similar movies ---
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:  # Skip the first movie (same movie)
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))

    return recommended_movie_names, recommended_movie_posters


# --- Streamlit App Title ---
st.title('🎬 Movie Recommender System')

# --- Load data ---
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# --- Dropdown to select a movie ---
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Search or select a movie from the dropdown ",
    movie_list
)

# --- Button to show recommendations ---
if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie)

    # Display posters in one row with larger size
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, width=200)  # Adjust width as needed (200-300)
            st.text(name)
