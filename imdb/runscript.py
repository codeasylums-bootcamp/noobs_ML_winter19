import requests
import json
from pprint import pprint
#get


while 1:
    a = int(input("enter a choice \n 1: get\n2: post\n3:delete\n4:put\n5:exit\n"))
    if a==1:
        print(a)
        r = requests.get('http://127.0.0.1:8000/imdbapp/4/') 

        pprint(r.text)




    if a == 2:
        #post
        payload={
            "movie_name": "The Matrix is a good movie",
            "movie_runtime": 136,
            "movie_genre": "action",
            "movie_rating": 8.7
            }
        r = requests.post("http://127.0.0.1:8000/imdbapp/", data=payload)
        #send some form form-encoded data, HTML form 


        # #example:-
        # url = 'https://api.github.com/some/endpoint'
        # payload = {'some': 'data'}

        # r = requests.post('http://127.0.0.1:8000/imdbapp/4/', data=json.dumps(payload))


        #
        #
        #
        #delete

    if a==3:
        # headers = {'content-type': 'application/json'}
        # url = 'http://127.0.0.1:8000/imdbapp/4'
        r = requests.delete(url=url)

        # response = requests.delete(
#     url, 
#     data=json.dumps(payload), 
#     headers=headers,
#     auth=HTTPBasicAuth(toggl_token, 'api_token')
# )


#put
    if a==4:
        payload = {"movie_name": "The Matrix is a good movie",
            "movie_runtime": 136,
            "movie_genre": "action",
            "movie_rating": 8.7}

        r = requests.put("http://127.0.0.1:8000/imdbapp/4", data=payload)

# You can then check the response status code with:

# r.status_code

# or the response with:

# r.content
    if a==5:
        break;