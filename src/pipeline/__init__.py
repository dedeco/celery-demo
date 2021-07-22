from flask import Blueprint
from flask_restful import Api
from .pipeline import AddNumbers, TaskManager

api_bp = Blueprint('api_bp', __name__)
api = Api(api_bp)
api.add_resource(AddNumbers, '/numbers')
api.add_resource(TaskManager, '/tasks')
