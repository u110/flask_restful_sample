from flask_restful import abort
from logzero import logger

from my_restful.dao import TodoDao


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TodoDao.get().todos:
        abort(404, message="Todo %s doesn't exist." % (todo_id))
