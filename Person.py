from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://x:123@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(), nullable=False)
    
    def __repr__(self):
        text = "<Person ID {}, name {}".format(self.id, self.password)
        return text
    
db.create_all()


new = Person(password="ahmed")
db.session.add(new)
db.session.commit()
db.session.close()

@app.route('/')
def index():
    n = Person.query.first()
    return n

if __name__ == '__main__':
    app.run()
