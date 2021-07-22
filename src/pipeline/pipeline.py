from flask_restful import reqparse
from http import HTTPStatus

from flask import url_for
from flask_restful import Resource

from src.tasks.add import add


class AddNumbers(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('a', type=int)
        parser.add_argument('b', type=int)
        args = parser.parse_args()
        task = add.apply_async((args.get('a'), args.get('b')), countdown=3)
        return {'url': url_for('api_bp.taskmanager',
                               task_id=task.id)}, HTTPStatus.ACCEPTED


class TaskManager(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task_id')
        args = parser.parse_args()
        task = add.AsyncResult(args.get('task_id'))
        if task.state == 'PENDING':
            response = {
                'state': task.state,
                'result': None
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'result': task.info
            }
        else:
            response = {
                'state': task.state,
                'result': None
            }
        return response, \
               HTTPStatus.OK
