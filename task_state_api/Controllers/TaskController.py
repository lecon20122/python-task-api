from app import db
from Models.Task import Task, task_schema, tasks_schema
from flask import jsonify
from Enums.TaskStateEnums import TaskStateEnums

# add new task

backwordsStates = [
    TaskStateEnums.DONE.value,
    TaskStateEnums.ACTIVE.value,
    TaskStateEnums.DRAFT.value
]

notAllowedToDraft = [
    TaskStateEnums.DONE.value,
    TaskStateEnums.ACTIVE.value,
    TaskStateEnums.ARCHIVE.value,
]


def add_task(request):
    title = request.json['title']
    state = request.json['state']
    new_task = Task(state, title)
    db.session.add(new_task)
    db.session.commit()
    return task_schema.jsonify(new_task)

# get all tasks


def get_tasks(request):
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result)

#  get task by id


def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)

# Update Task


def update_task(request, id):
    task = Task.query.get(id)
    newTitle = request.json['title']
    newState = request.json['state']

    # from Draft to Done
    if task.state == TaskStateEnums.DRAFT.value and newState == TaskStateEnums.DONE.value:
        return ("not allowed to Change the state of this Task", 400)

    # from any state to draft
    if task.state in notAllowedToDraft and newState == TaskStateEnums.DRAFT.value:
        return ("not allowed to draft this Task", 400)

    # Archive cant go backwords
    if task.state == TaskStateEnums.ARCHIVE.value and newState in backwordsStates:
        return ("Archive cant go backwords", 400)

    task.title = newTitle
    task.state = newState
    db.session.commit()
    return task_schema.jsonify(task)

# get task by id


def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)
