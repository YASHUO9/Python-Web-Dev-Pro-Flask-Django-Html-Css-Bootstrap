from flask import Flask, render_template,request,redirect
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


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = TodoList(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    
    
    allTodo = TodoList.query.all()
    return render_template('index.html',alltodo=allTodo)


@app.route('/delete/<int:sno>')
def delete(sno):
    todo = TodoList.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')
    

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = TodoList.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    todo = TodoList.query.filter_by(sno=sno).first()
    return render_template('update.html',todo=todo)




@app.route('/show')
def show():
    allTodo = TodoList.query.all()
    print(allTodo)
    return  "This is the show page of the to do list app"




if __name__ == '__main__':
    app.run(debug=True)
    