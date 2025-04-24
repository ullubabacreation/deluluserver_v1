from flask import Flask, request, jsonify
from ytmusicapi import YTMusic
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ytmusic = YTMusic()

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Missing query parameter'}), 400
    results = ytmusic.search(query)
    return jsonify(results)

@app.route('/')
def home():
    return jsonify({"message": "Delulufy YTMusic API is running!"})

