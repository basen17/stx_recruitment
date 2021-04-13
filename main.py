from flask import Flask, render_template, jsonify
from flask_restful import Api, Resource, reqparse
import requests
import json

app = Flask(__name__)
api = Api(app)

# book_put_args = reqparse.RequestParser()
# book_put_args.add_argument("name")
dataset = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')
result = {}

# for data in dataset.json()['items']:
#     title = data['volumeInfo']['title']
#     result.append(title)
    # print (type(data['volumeInfo']['title']))
#print(sorted(result))

for data in dataset.json()['items']:
    title = data['volumeInfo']['title']
    result['title'] = title
    # print(title)

print(result)

# print(result)
# title_dict = dict.fromkeys(result, "title")
# print(title_dict)
# title_dict = {v: k for k, v in title_dict.items()}
# print(title_dict)

@app.route('/')
def home():
    return render_template('rectuitment.html')

@app.route('/book')
def GetAllBooks():
    for data in dataset.json()['items']:
        title = data['volumeInfo']['title']
        result.append(title)
        title_dict = dict.fromkeys(result, "title")
        title_dict = {v: k for k, v in title_dict.items()}
    print(sorted(title_dict))
    return 0 #jsonify("title" : [result])


# if __name__ == '__main__':
#     app.run(debug=True)