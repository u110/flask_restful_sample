# -*- coding: UTF-8 -*-

from flask import Flask
from flask_restful import Resource, Api
from my_restful.todo import Todo, TodoList

app = Flask(__name__)

api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {
            'hello': 'world'
        }


api.add_resource(HelloWorld, "/")

api.add_resource(TodoList, "/todos")
api.add_resource(Todo, "/todo", "/todo/<string:todo_id>")


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
