from flask_restful import Resource
from services.utils import read_file
from models.link import Link


class LinkRes(Resource):
    def get(self):
        data = read_file('data/links.csv')
        link_list = []
        for link in data[1:]:
            link_obj = (Link(link.split(',')[0], link.split(',')[1], link.split(',')[2])).__dict__
            link_list.append(link_obj)
        return link_list
