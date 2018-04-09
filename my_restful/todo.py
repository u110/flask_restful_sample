from flask import request
from flask_restful import Resource
from logzero import logger

from my_restful.dao import TodoDao
from my_restful.base import abort_if_todo_doesnt_exist


class TodoList(Resource):

    def get(self):
        my_todos = TodoDao.get().todos
        return my_todos


def req(key):
    if request.is_json:
        return request.json.get(key)
    else:
        return request.form.get(key)

class Todo(Resource):

    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        my_todos = TodoDao.get().todos
        todo = my_todos.get(todo_id)
        logger.debug(todo)

        return {todo_id: todo}

    def post(self):
        my_todos = TodoDao.get().todos
        new_todo = req("data")
        new_id = len(my_todos) + 1
        new_id = str(new_id)
        my_todos[new_id] = new_todo
        return {new_id: new_todo}


    def put(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        my_todos = TodoDao.get().todos
        val = req("data")
        logger.debug("val: %s" % val)
        my_todos[todo_id] = val
        return {todo_id: val}, 201
