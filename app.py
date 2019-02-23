
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from datetime import datetime , timedelta,date
import time
import datetime as dt
#from flask_optional_routes import OptionalRoutes

from config import sqluser,sqlpassword,dbport,dburi,dbname
from flask import Flask, render_template, redirect
from flask_table import Table, Col
import pymysql
pymysql.install_as_MySQLdb()
#################################################
# Database Setup
#################################################
engine = create_engine(f"mysql://{sqluser}:{sqlpassword}@{dburi}:{dbport}/{dbname}")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Youtube_Summary = Base.classes.youtube_summary

# Create our session (link) from Python to the DB
session = scoped_session(sessionmaker(engine))


from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    category = Col('category')
    views = Col('views')
    likes= Col('likes')
    dislikes=Col('dislikes')
    comment_count=Col('comment_count')


results = session.query(Youtube_Summary.category,Youtube_Summary.views, Youtube_Summary.likes,Youtube_Summary.dislikes,Youtube_Summary.comment_count).all()
table= ItemTable(results)
print(table.__html__())
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    #prcp = {category:views for category,views in results}
    table=ItemTable(results)
    return render_template("index.html", table=table)
if __name__ == '__main__':
    app.run(debug=True)
