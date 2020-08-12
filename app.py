
import numpy as np
import pandas as pd
 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, render_template, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import create_classes

from config import username, password

#https://stackabuse.com/using-sqlalchemy-with-flask-and-postgresql/
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@localhost:5432/movies'
db = SQLAlchemy(app)
moviedata = create_classes(db)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/svm")
def bar():
        return render_template('svm.html')

@app.route("/dl")
def bubble():
        return render_template('dl.html')

@app.route("/logistic")
def map():
        return render_template('logistic.html')

@app.route("/data-table")
def data():
        return render_template('data-table.html')

@app.route("/raw-data")
def data_retrieval():
        results = db.session.query(moviedata.id, moviedata.imdb_title_id, moviedata.title, moviedata.year, moviedata.genre, moviedata.duration, moviedata.country, moviedata.director, moviedata.production_company, moviedata.budget, moviedata.total_votes, moviedata.median_vote, moviedata.all18to29, moviedata.all30to44, moviedata.allover45, moviedata.males, moviedata.males18to29, moviedata.males30to44, moviedata.malesover45, moviedata.females, moviedata.females18to29, moviedata.females30to44, moviedata.femalesover45, moviedata.rating_class).all()
        # initialize dictionary 
        data = []
        for result in results:
                d = {"id":result[0], "imdb_title_id":result[1], "title" : result[2], "year" : result[3], "genre" : result[4], "duration" : result[5], "country" : result[6], "director" : result[7], "production_company" : result[8], "budget":result[9], "total_votes":result[10], "median_vote" : result[11], "all18-29" : result[12], "all30to44" : result[13], "allover45" : result[14], "males" : result[15], "males18to29" : result[16], "males30to44" : result[17], "malesover45":result[18], "females":result[19], "females18to29" : result[20], "females30to44" : result[21], "femalesover45" : result[22], "rating_class" : result[23]} 
                data.append(d)
        json_data = jsonify(data)
        return json_data

if __name__ == '__main__':
    app.run()