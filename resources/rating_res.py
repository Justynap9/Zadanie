from flask_restful import Resource
from services.utils import read_file
from models.rating import Rating


class RatingRes(Resource):
    def get(self):
        data = read_file('data/ratings.csv')
        rating_list = []
        for rating in data[1:]:
            rating_obj = (Rating(rating.split(',')[0], rating.split(',')[1], rating.split(',')[2], rating.split(',')[3])).__dict__
            rating_list.append(rating_obj)
        return rating_list
