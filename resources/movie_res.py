from flask_restful import Resource
from services.utils import read_file
from models.movie import Movie


class MovieRes(Resource):
    def get(self):
        data = read_file('D:/movies.csv')
        movie_list = []
        for movie in data[1:]:
            movie_obj = (Movie(movie.split(',')[0], movie.split(',')[1], movie.split(',')[2])).__dict__
            movie_list.append(movie_obj)
        return movie_list
