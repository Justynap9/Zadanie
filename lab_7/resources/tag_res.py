from flask_restful import Resource
from services.utils import read_file
from models.tag import Tag


class TagRes(Resource):
    def get(self):
        data = read_file('D:/tags.csv')
        tag_list = []
        for tag in data[1:]:
            tag_obj = (Tag(tag.split(',')[0], tag.split(',')[1], tag.split(',')[2], tag.split(',')[3])).__dict__
            tag_list.append(tag_obj)
        return tag_list
