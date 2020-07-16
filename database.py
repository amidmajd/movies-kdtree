import imdb


moviesDB = imdb.IMDb()

# movies = moviesDB.search_movie("")

# mID = movies[0].getID()
# movie = moviesDB.get_movie(mID)
print(dir(moviesDB))
print(moviesDB.get_top())