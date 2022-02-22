import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import Controllers.TaskController as TaskController

# init App
app = Flask(__name__)

# Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init db
db = SQLAlchemy(app)

# init Marshmellow
marshmellow = Marshmallow(app)


@app.route('/task', methods=['POST', 'OPTIONS'])
def add_task():
    return TaskController.add_task(request=request)


@app.route('/tasks', methods=['GET', 'OPTIONS'])
def get_tasks():
    return TaskController.get_tasks(request=request)


@app.route('/task/<int:id>', methods=['GET'])
def get_task(id: int):
    return TaskController.get_task(id)


@app.route('/task/update/<id>', methods=['PUT'])
def update_task(id: int):
    return TaskController.update_task(request=request, id=id)


@app.route('/task/delete/<id>', methods=['DELETE'])
def delete_task(id: int):
    return TaskController.delete_task(id=id)


# Run Server
if (__name__ == '__main__'):
    app.run(debug=True)
