from TwitterAPI import TwitterAPI, TwitterRequestError, TwitterConnectionError

class TwitterConnection:
        '''
        Class for connecting to Twitter and retrieving info.

        Args:
                keys (dict of str: str): Keys for authentication with Twitter.


        Attributes:
                api (TwitterAPI): Connection instance.
        '''

        api = None

        def __init__(self, keys):

                self.api = TwitterAPI(
                        keys['consumer'],
                        keys['consumer_secret'],
                        keys['access_token'],
                        keys['access_token_secret'],
                        api_version='2')

        def request(self, endpoint, params = None):
                '''Make a request to the Twitter API

                Args:
                        endpoint (str) : Twitter API endpoint.
                        params (dict) : Parameters for request.

                Returns:
                        Response (TwitterAPI.TwitterResponse).
                '''

                try:
                        response = self.api.request(endpoint, params=params)

                        # Iterate through response to generate error if there is one.
                        for item in response:
                                pass
                except (TwitterRequestError, TwitterConnectionError) as e:
                        return(e)

                return response
