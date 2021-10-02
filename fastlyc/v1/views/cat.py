from flask_restx import Namespace, Resource, fields
from fastlyc.v1.helper import logger

ns = Namespace('cat', '这是猫')


@ns.route('/')
class Cat(Resource):

    @ns.doc('')
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
