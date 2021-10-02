from flask import request
import os
from flask_restx import Namespace, Resource, fields, reqparse
from fastlyc.v1.helper import logger

from fastlyc.v1.models.dog_model import DogModel

ns = Namespace('dog', '这是狗')


class UrgenItem(fields.Raw):
    xname = fields.Integer

    def format(self, v):
        return 'urgent'+str(v)


dog_model = ns.model('dog', {
    'id': fields.Integer(required=True),
    # x为Dict 表示传入的 {'id': 12, 'private_name': '122', 'age': 10}
    # 'name': UrgenItem(attribute='private_name', default=None),
    'name': fields.String(default=None),
    'age': fields.List(fields.Integer, default=[]),
    # 递归自身
    # fields.Nested(xx_model) 实际上等于 fields.Raw(title='xx_model_name')
    # Nested接受一个字典
    'child': fields.List(fields.Raw(title='dog'), default=None)
})


@ns.route('/')
class Dog(Resource):

    dog_get = reqparse.RequestParser()
    dog_get.add_argument('id', type=int, required=True, location='args')
    dog_get.add_argument('name', type=str, required=True, location='args')

    @ns.marshal_with(dog_model)
    @ns.expect(dog_get, validate=True)
    def get(self):
        x = self.dog_get.parse_args()

        d = DogModel.query.filter_by(id=1).first()
        logger.info(d)

        return {'id': 12, 'child': [{'id': 12}]}

    @ns.expect(dog_model, validate=True)
    def post(self):
        x = ns.payload
        print(x)
        return 'fine'

    def put(self):
        pass

    def delete(self):
        pass
