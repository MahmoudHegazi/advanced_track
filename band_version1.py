#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from db_class import Band, Event, db, app
import requests
import os
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/ok', methods=['POST'])
def ader():
    if request.method == 'POST':
        # image part
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            url=UPLOAD_FOLDER+'/'+filename
        if url:
            return '<h2>Band: {}</h2><h5>Title: {}</h5><h4>Image: </h4><img src="{}" alt="{}" style="margin-left:auto;margin-right:auto;">'.format(request.form['band'],request.form['title'],url,request.form['band'])
        return redirect(url_for('index', message="image_not_added"))
    return False

# like is noob becuase it like filter_by
# Car.query.filter(Car.car.like('BMW')).all()
# search match any exist  use this % some text %
# Car.query.filter(Car.car.match('%bmw%')).all()
#return redirect(request.url)
# session.rollback() cancel the session.add uimportant


if __name__ == '__main__':
    app.secret_key = 'S&Djry636qyye21777346%%^&&&#^$^^y___'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
