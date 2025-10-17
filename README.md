# 🎬 Movie Recommender System

This is a **Movie Recommender System** built with Python and Streamlit.  
It suggests similar movies based on a **Content-Based Filtering** approach, leveraging movie metadata like genres, keywords, cast, and crew.

---

## 🔹 Features

- Suggests **5 similar movies** based on the selected movie.  
- Displays **movie posters, title, release year, and rating**.  
- **Handles missing posters gracefully** with placeholders.  
- Built with **Streamlit**, making it interactive and easy to use.  
- **Large poster images** displayed in a single row for better visualization.  

---

## 🔹 How It Works

The system uses a **Content-Based Recommendation** approach:  

1. Movie metadata such as **genres, keywords, cast, and crew** are extracted.  
2. Text data is **processed into numerical vectors** using `CountVectorizer` and stemming.  
3. **Cosine Similarity** is calculated between movies to find the most similar ones.  
4. When a movie is selected, the system fetches **poster images from TMDB** and displays the top 5 recommendations.

---

## 🔹 Dataset

The dataset used for this project is from **TMDB Movie Metadata**:

[TMDB Movie Metadata on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

- Contains metadata of 10,000+ movies including title, genres, cast, crew, keywords, budget, and revenue.  
- Preprocessing is done to extract relevant features for content-based recommendations.

---

## 🔹 Installation & Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py


Select a movie from the dropdown to get 5 recommended movies with posters, release year, and rating.

🔹 Screenshots
Example Output:
Screenshot 1	Screenshot 2

	

Replace screenshots/output1.png with your actual images.

🔹 Technologies Used

Python 3

Pandas

Requests

Streamlit

TMDB API

🔹 Notes

You need a TMDB API Key to fetch movie posters.

Missing posters are handled with placeholder images.

Content-based filtering is efficient for recommending movies with rich metadata.

🔹 Author

Harshitha Nuthikadi
