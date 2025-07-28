import streamlit as st

# ✅ Page Configuration
st.set_page_config(page_title="🎥 Movie Recommendation", layout="wide")
st.title("🎬 Movie Recommendation App")

# ✅ Step 1: Movie Dataset
movie_data = {
    "Titanic": {
        "genre": "romance",
        "image": "titanic.jpg",
        "rating": 7.8,
        "year": 1997,
        "trailer": "https://www.youtube.com/watch?v=kVrqfYjkTdQ"
    },
    "Inception": {
        "genre": "action",
        "image": "inception.jpg",
        "rating": 8.8,
        "year": 2010,
        "trailer": "https://www.youtube.com/watch?v=YoHD9XEInc0"
    },
    "Avengers": {
        "genre": "action",
        "image": "avenger.jpg",
        "rating": 8.0,
        "year": 2012,
        "trailer": "https://www.youtube.com/watch?v=eOrNdBpGMv8"
    },
    "La La Land": {
        "genre": "music",
        "image": "lalaland.jpg",
        "rating": 8.0,
        "year": 2016,
        "trailer": "https://www.youtube.com/watch?v=0pdqf4P9MB8"
    },
    "John Wick": {
        "genre": "thriller",
        "image": "johnwick.jpg",
        "rating": 7.4,
        "year": 2014,
        "trailer": "https://www.youtube.com/watch?v=2AUmvWm5ZDQ"
    },
    "The Notebook": {
        "genre": "romance",
        "image": "the_notebook.jpg",
        "rating": 7.8,
        "year": 2004,
        "trailer": "https://www.youtube.com/watch?v=FC6biTjEyZw"
    },
    "Iron Man": {
        "genre": "action",
        "image": "ironman.jpg",
        "rating": 7.9,
        "year": 2008,
        "trailer": "https://www.youtube.com/watch?v=8hYlB38asDY"
    },
   
    "The Conjuring": {
        "genre": "horror",
        "image": "the_conjuring.jpg",
        "rating": 7.5,
        "year": 2013,
        "trailer": "https://www.youtube.com/watch?v=k10ETZ41q5o"
    },
    "Coco": {
        "genre": "animation",
        "image": "coco.jpg",
        "rating": 8.4,
        "year": 2017,
        "trailer": "https://www.youtube.com/watch?v=Rvr68u6k5sI"
    },
    "Frozen": {
        "genre": "animation",
        "image": "frozen.jpg",
        "rating": 7.4,
        "year": 2013,
        "trailer": "https://www.youtube.com/watch?v=TbQm5doF_Uc"
    },
    "Moana": {
        "genre": "animation",
        "image": "moana.jpg",
        "rating": 7.6,
        "year": 2016,
        "trailer": "https://www.youtube.com/watch?v=LKFuXETZUsI"
    },
    "The Dark Knight": {
        "genre": "action",
        "image": "thedarkknight.jpg",
        "rating": 9.0,
        "year": 2008,
        "trailer": "https://www.youtube.com/watch?v=EXeTwQWrcwY"
    },
    "Joker": {
        "genre": "thriller",
        "image": "joker.jpg",
        "rating": 8.5,
        "year": 2019,
        "trailer": "https://www.youtube.com/watch?v=zAGVQLHvwOY"
    },
    "Zindagi Na Milegi Dobara": {
        "genre": "drama",
        "image": "zindagi.jpg",
        "rating": 8.2,
        "year": 2011,
        "trailer": "https://www.youtube.com/watch?v=FJrpcDgC3zU"
    },
    "3 Idiots": {
        "genre": "comedy",
        "image": "3idiots.jpg",
        "rating": 8.4,
        "year": 2009,
        "trailer": "https://www.youtube.com/watch?v=xvszmNXdM4w"
    },
    "PK": {
        "genre": "comedy",
        "image": "pk.jpg",
        "rating": 8.1,
        "year": 2014,
        "trailer": "https://www.youtube.com/watch?v=SOXWc32k4zA"
    },
    
    "Bhool Bhulaiyaa": {
        "genre": "horror",
        "image": "bhoolbhulaiyaa.jpg",
        "rating": 7.4,
        "year": 2007,
        "trailer": "https://www.youtube.com/watch?v=Jb4zU1jTiG8"
    },
    "Barfi": {
        "genre": "romance",
        "image": "barfi.jpg",
        "rating": 8.1,
        "year": 2012,
        "trailer": "https://www.youtube.com/watch?v=ESIjWQ2HZmE"
    }
}

# ✅ Step 2: Genre Dropdown
all_genres = sorted(set(movie["genre"] for movie in movie_data.values()))
selected_genre = st.selectbox("🎞️ Select Genre", ["All"] + all_genres)

# ✅ Step 3: Filter Movies
if selected_genre == "All":
    filtered_movies = list(movie_data.items())
else:
    filtered_movies = [(title, data) for title, data in movie_data.items() if data["genre"] == selected_genre]

# ✅ Step 4: Display Movies in Grid
for i in range(0, len(filtered_movies), 3):
    cols = st.columns(3)
    for col, (title, data) in zip(cols, filtered_movies[i:i+3]):
        with col:
            try:
                st.image(data["image"], caption=title, use_container_width=True)
            except Exception as e:
                st.warning(f"❌ Could not load image for **{title}**: {e}")
            st.markdown(f"**🎭 Genre:** {data['genre'].capitalize()}")
            st.markdown(f"**⭐ Rating:** {data['rating']}")
            st.markdown(f"**📅 Year:** {data['year']}")
            st.markdown(f"[▶️ Watch Trailer]({data['trailer']})", unsafe_allow_html=True)
