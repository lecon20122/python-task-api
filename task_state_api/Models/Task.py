from app import db
from Enums import TaskStateEnums
from app import marshmellow


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    state = db.Column(db.Enum('draft', 'active', 'done',
                      'archived', name='TaskStateEnums'))

    def __init__(self, state, title):
        self.title = title
        self.state = state


class TaskSchema(marshmellow.Schema):
    class Meta:
        fields = ('id', 'state', 'title')


# init Schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


db.create_all()
