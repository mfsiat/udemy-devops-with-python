from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def list1():
    todo_list = Todo.query.all()
    return render_template("list.html", todo_list=todo_list)

@app.route('/edit')
def edit():
    todo_list = Todo.query.all()
    return render_template("base.html")

# base
@app.route('/base')
def base():
    return render_template("base.html")

if __name__ == "__main__":
    app.run()
