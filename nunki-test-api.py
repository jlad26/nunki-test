from flask import Flask, request
from flask_restful import Resource, Api
from TwitterConnection import TwitterConnection
import constants as C # Contains single constant KEYS for Twitter authentication

app = Flask(__name__)
api = Api(app)

class User(Resource):

    def get(self, username):
        connection = TwitterConnection(C.KEYS)
        url = f"users/by/username/:{username}"

        users = []
        for item in connection.request(url):
            users.append(item)
        
        if users:

            user = users[0]
            url = f"users/:{user['id']}/tweets"
            user_content = []
            for item in connection.request(url):
                user_content.append(item)
            return user_content

        else:
            
            return 'User not found'

class Keyword(Resource):

    def get(self):

        if 'q' not in request.args:

            return 'To use search, please use the query parameter q to specify your search term'

        else:
            connection = TwitterConnection(C.KEYS)
            url = f"tweets/search/recent"
            params = {
                'query' : request.args['q'],
                'tweet.fields':'author_id',
                'expansions':'author_id'
            }

            results = []
            for item in connection.request(url, params=params):
                results.append(item)

            return results

api.add_resource(User, '/users/<string:username>')
api.add_resource(Keyword, '/search')

if __name__ == '__main__':
    app.run(debug=True)