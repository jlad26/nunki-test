from flask import Flask, request, abort
from TwitterConnection import TwitterConnection
import constants as C # Contains single constant KEYS for Twitter authentication

app = Flask(__name__)

@app.route('/users/<string:username>')
def get_user_content(username):
    '''Gets the tweets belong to a Twitter user.

    First gets user id, then gets tweets belonging to that user id.

    Args:
        username (str) : User twitter handle.

    Returns:
        User info and tweets.
    '''

    url = f"users/by/username/:{username}"

    output = {
        'messages' : [],
        'tweets' : [],
        'user' : None
    }

    users_response = connection.request(url)
    users = []

    # Differentiate between user info and warning / error messages.
    for item in users_response:
        if 'username' in item:
            users.append(item)
        else:
            output['messages'].append(item)
    
    # Check that something has been returned.
    if users:

        user = users[0]

        # Check that response is a user.
        if 'username' not in user:
            abort(404, description = user)
        else:

            output['user'] = user
            
            url = f"users/:{user['id']}/tweets"

            tweets_response = connection.request(url)

            for item in tweets_response:
                
                # Differentiate between tweets and warning / error messages.
                if 'text' in item or 'full_text' in item:
                    output['tweets'].append(item)
                else:
                    output['messages'].append(item)

    return output

@app.route('/search')
def search():
    '''Searches for Twitter tweets containing a keyword.

    The keyword is passed via the parameter 'q' in the query string and
    and is available in the dictionary request.args.

    Returns:
        Tweets contining a keyword
    '''

    output = {
        'messages' : [],
        'tweets' : []
    }

    if 'q' not in request.args:

        abort(401, 'To use search, please use the query parameter q to specify your search term')

    else:

        url = f"tweets/search/recent"
        params = {
            'query' : request.args['q'],
            'tweet.fields':'author_id',
            'expansions':'author_id'
        }

        # Differentiate between tweets and warning / error messages.
        for item in connection.request(url, params=params):
            if 'text' in item or 'full_text' in item:
                output['tweets'].append(item)
            else:
                output['messages'].append(item)

        return output

connection = TwitterConnection(C.KEYS)

if __name__ == '__main__':
    app.run(debug=True)