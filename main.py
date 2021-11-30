from flask import Flask
from flask_restful import Api
from resources.movie_res import MovieRes
from resources.link_res import LinkRes
from resources.tag_res import TagRes
from resources.rating_res import RatingRes

app = Flask(__name__)
api = Api(app)

api.add_resource(MovieRes, '/movies')
api.add_resource(LinkRes, '/links')
api.add_resource(TagRes, '/tags')
api.add_resource(RatingRes, '/ratings')

if __name__ == '__main__':
    app.run(debug=True)
