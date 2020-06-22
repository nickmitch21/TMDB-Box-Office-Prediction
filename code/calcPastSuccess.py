import pandas as pd
import imdb
import time


def getPastSuccess(movie, ia):
    start_time = time.time()
    for i in range(8):
        actor = movie['cast'][i]
        filmList = ia.get_person_filmography(actor.getID())['data']['filmography'][0]
        filmography = filmList.get('actor')
        if filmography is None:
            filmography = filmList.get('actress')

        totalRating = 0
        totalBO = 0
        movieCount = 0
        accMovieCount = 0
        for film in filmography:
            if film['kind'] == 'movie':
                film = ia.get_movie(film.getID())
                rating = film.get("rating")
                boxOffice = film.get("box office")
                if boxOffice is not None :
                    gross = boxOffice.get('Cumulative Worldwide Gross')
                else:
                    gross = None

                accMovieCount += 1
                if rating is not None and gross is not None:
                    totalRating += float(rating)
                    gross = gross.split(' ')[0][1:].replace(',','')
                    totalBO += float(gross)
                    movieCount += 1
        if movieCount > 0:
            AvgIMDbScore = totalRating/movieCount
            AvgBO = totalBO/movieCount
        else:
            AvgIMDbScore = 0
            AvgBO = 0
        print("Statistics for", actor)
        print('Number of Movies used in formula: ',movieCount)
        print('Number of Movies Total: ', accMovieCount)
        print("Average IMDb Score: ", AvgIMDbScore)
        pastIMDbFormula = AvgIMDbScore - 10 * (1/3)**movieCount
        pastBoxOfficeFormula = 10* (AvgBO / 100000000) - 10 * (1/3)**movieCount

        print('IMDb Weighted Average Rating for: ', pastIMDbFormula)
        print('Box Office Weighted Average for: ', pastBoxOfficeFormula)
        print("--- %s minutes ---" % ((time.time() - start_time)/60))
        print()
