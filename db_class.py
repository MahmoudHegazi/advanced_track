from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://x:123@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config["IMAGE_UPLOADS"] = 'uploads'
db = SQLAlchemy(app)

class Band(db.Model):
  __tablename__ = 'band'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  image = db.Column(db.String(), nullable=False)
  title = db.Column(db.String())
  def __repr__(self):
    return "<Band ID: {}, name: {}>".format(self.id, self.name)


class Event(db.Model):
  __tablename__ = 'event'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  date = db.Column(db.String())
  image = db.Column(db.String())
  band_id = db.Column(db.Integer, db.ForeignKey('band.id'))

  def __repr__(self):
    return "<Car ID: {}, name: {}, Band Id:{}>".format(self.id, self.name, self.band_id)
db.create_all()
