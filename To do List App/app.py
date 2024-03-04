from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt


#<-----------------------------------To do List App------------------------------------->

# CRUD:
# Create
# Read
# Update
# Delete



app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"


db = SQLAlchemy(app)


class TodoList(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f'{self.sno} - {self.title}'


#<-----------------------------------To do List App------------------------------------->


@app.route('/')
def index():
    
    allTodo = TodoList.query.all()
    return render_template('index.html',alltodo=allTodo)



@app.route('/show')
def show():
    allTodo = TodoList.query.all()
    print(allTodo)
    return  "This is the show page of the to do list app"









if __name__ == '__main__':
    app.run(debug=True)
    