# Spotify Song Popularity Classifier

Can a song's audio features predict how popular it will be? This mini-project
trains classifiers on the most-streamed Spotify songs of 2023 to find out.

Group mini-project (Group 9) for NTU's Introduction to Data Science and
Artificial Intelligence course.

## Approach

1. **Data:** about 950 songs from the Kaggle
   [Top Spotify Songs 2023](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)
   dataset (`spotify-2023.csv`).
2. **Features:** danceability, valence, energy, acousticness,
   instrumentalness and speechiness.
3. **Target:** songs are split into three popularity classes (low, medium,
   high) at the 33rd and 66th percentiles of stream count.
4. **Exploration:** correlation heatmap, pair plot and per-feature
   distributions by class.
5. **Models:**
   - K-Nearest Neighbours on standardised features, with k chosen from 1 to 30
   - Random Forest tuned with 5-fold `GridSearchCV`
   - Soft-voting ensemble of the two
6. **Interpretation:** permutation importance for each model.
7. **Demo:** a small function that takes a song's features and returns its
   predicted popularity class.

## Results

On a held-out test set of 236 songs:

| Model | Accuracy |
| --- | --- |
| K-Nearest Neighbours (k = 6) | 0.43 |
| Random Forest | 0.39 |
| Ensemble (KNN + Random Forest) | 0.43 |

Random guessing across three balanced classes gives about 0.33, so the models
find some signal, but not much. The main finding is that audio features alone
are weak predictors of streams. Popularity depends heavily on things this
feature set leaves out, such as the artist's existing audience, playlist
placement and release timing.

## Files

| File | Contents |
| --- | --- |
| `nullnvoid.ipynb` | Full notebook: cleaning, plots, models and results (the figures above) |
| `IE005_GROUP9.ipynb` | Group submission version of the notebook |
| `spotify-2023.csv` | Dataset |

## Running it

```bash
pip install -r requirements.txt
jupyter notebook nullnvoid.ipynb
```

## Built with

Python, pandas, NumPy, scikit-learn, seaborn, Matplotlib
