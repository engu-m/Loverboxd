# Loverboxd 🎥🌟💌

This is a simple movie recommender system tailored to members of [Letterboxd](https://letterboxd.com), a social network for cinema lovers. While the website is complete, it lacks an important feature, both with free and paid subscriptions: movie recommendation. This project aims to make up for it.

Sidenote: The official answer to this is [here](https://letterboxd.com/about/faq/#recommendations) but it is not satisfactory either.

<!-- All you will need is a Letterboxd account with several movies rated. The more the better. Then you have to export your data and upload here (website to come) the file ``reviews.csv`` -->

## How does it work?

### Installation

Download the dataset from [here](https://www.kaggle.com/samlearner/letterboxd-movie-ratings-data) and unzip it. Move the csv files in a new folder called `letterboxd_data`

Install the requirements with
```pip install -r requirements.txt```

[Export](https://letterboxd.com/settings/data/) your letterboxd account data. Move the file `ratings.csv` in the folder `user_data`. Then launch `reco_surprise.ipynb`


### Motivation

While looking for datasets to achieve my needs, I came across [this repository](https://github.com/sdl60660/letterboxd_recommendations) with the corresponding [up-and-running website](https://letterboxd.samlearner.com/). This is actually very close to the end result I intended. However, just because someone else had the idea before does not mean I cannot do it myself! For this reason I did not look at his code and coded the thing from scratch. Another good motivation is that I wish additional features, such as filtering my recommendations by movie duration, importings filter settings, have more than 50 recommendation results, etc.


### Algorithms

Several algorithms are proposed, from easiest to more advanced.

I suggest [this great tutorial](https://realpython.com/build-recommendation-engine-collaborative-filtering/) to get started with most simple recommender systems. Even the most basic system gives good results for a single user.

## What's next (other branches)

- updated database for movies released in 2023 or later
- accurate filters for movie results
- web app deployment with flask and heroku
- online hosting of database
