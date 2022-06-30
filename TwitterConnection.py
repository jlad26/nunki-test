from TwitterAPI import TwitterAPI, TwitterRequestError, TwitterConnectionError

class TwitterConnection:

        api = None

        def __init__(self, keys):
                try:
                        self.api = TwitterAPI(
                                keys['consumer'],
                                keys['consumer_secret'],
                                keys['access_token'],
                                keys['access_token_secret'],
                                api_version='2')
                
                except TwitterConnectionError as e:
                        print(e)
        
                except Exception as e:
                        print(e)

        def request(self, endpoint, params = None):
                try:

                        if params == None:
                                return self.api.request(endpoint)
                        else:
                                return self.api.request(endpoint, params)
                
                except TwitterRequestError as e:
                        print(e)
                
                except Exception as e:
	                print(e)
