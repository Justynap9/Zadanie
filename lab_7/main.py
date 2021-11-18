from flask import Flask
from flask_restful import Resource, Api
from services.utils import read_file
from movie import Movie

app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        data = read_file('D:/movies.csv')
        movie_list = []
        for movie in data.split('/n'):
            movies = movie.splitlines()
            for line in movies[1:]:
                elements = line.split(',')
                movie_obj = Movie(elements[0], elements[1], elements[2]).__dict__
                movie_list.append(movie_obj)
            return movie_list

api.add_resource(Main, '/')

if __name__ == '__main__':
    app.run(debug=True)
