from flask import Flask, render_template, jsonify, request
from flask_restful import Api, Resource, reqparse
import requests
import json
import collections

app = Flask(__name__)
api = Api(app)


dataset = requests.get('https://www.googleapis.com/books/v1/volumes?q=Hobbit')


@app.route('/book', methods=['GET'])
def GetAllBooks():
    published_date = request.args.get('published_date')
    sort = request.args.get('sort')
    authors = request.args.get('authors').encode()
    if (published_date):
        result = []
        for data in dataset.json()['items']:
            if published_date == data['volumeInfo']['publishedDate']:
                result.append(data['volumeInfo']['title'])
        return jsonify({'books' : result})        

    elif (sort):
        result = {}
        titles_list = []
        published_date_list = []
        for data in dataset.json()['items']:
            titles_list.append(data['volumeInfo']['title'])
            published_date_list.append(data['volumeInfo']['publishedDate'])
            pair_lists = zip(titles_list, published_date)
            result_dict = dict(pair_lists)
            result = collections.OrderedDict(sorted(result_dict.items()))
        return jsonify({ "books" : result})


    elif (authors):
        result = []
        for data in dataset.json()['items']:
            string_data = str(data['volumeInfo']['authors'])
            if authors == string_data.encode():
                result.append(data['volumeInfo']['title'])
        return jsonify({ "books" : result})

    else:
        result = []
        for data in dataset.json()['items']:
            result.append(data['volumeInfo']['title'])
        return jsonify({ "books" : result})


@app.route('/book/<id>', methods=['GET'])
def GetBookById(id):
    result = {}
    for data in dataset.json()['items']:
        if data['id'] == id:
            result["data"] = data["volumeInfo"]
    return jsonify( result )

        

if __name__ == '__main__':
    app.run(debug=True)