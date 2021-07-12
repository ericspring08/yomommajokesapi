from flask import Flask, jsonify
import json
import random
from flask_cors import CORS

jokes = json.load(open('./jokes.json',))
app = Flask(__name__)
CORS(app)

categories_list = ("fat", "stupid", "ugly", "nasty", "old", "hairy", "poor", "short", "skinny", "tall")
@app.route("/")
def index():
    category = random.choice(categories_list)
    return jsonify({"jokes": random.choice(jokes[category])})

@app.route("/categories")
def categories():
    return {
        "categories": [
            "fat", 
            "stupid", 
            "ugly", 
            "nasty", 
            "old", 
            "hairy", 
            "poor", 
            "short", 
            "skinny", 
            "tall"
        ]
    }

@app.route("/fat")
def fat():
    return jsonify({"jokes" : random.choice(jokes["fat"])})


@app.route("/stupid")

def stupid():
    return jsonify({"jokes" : random.choice(jokes["stupid"])})

@app.route("/ugly")

def ugly():
    return jsonify({"jokes" : random.choice(jokes["ugly"])})

@app.route("/nasty")

def nasty():
    return jsonify({"jokes" : random.choice(jokes["nasty"])})

@app.route("/old")

def old():
    return jsonify({"jokes" : random.choice(jokes["old"])})

@app.route("/hairy")

def hairy():
    return jsonify({"jokes": random.choice(jokes["hairy"])})
    
@app.route("/poor")

def poor():
    return jsonify({"jokes" : random.choice(jokes["poor"])})

@app.route("/short")

def short():
    return jsonify({"jokes" : random.choice(jokes["short"])})

@app.route("/skinny")

def skinny():
    return jsonify({"jokes" : random.choice(jokes["skinny"])})

@app.route("/tall")

def tall():
    return jsonify({"jokes" : random.choice(jokes["tall"])})
if __name__ == '__main__':
        
    app.run()