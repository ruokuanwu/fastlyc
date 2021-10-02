from flask import Blueprint, abort
from flask_restx import Api, Resource
from fastlyc.v1.helper import logger

from fastlyc.v1.views.cat import ns as cat_ns
from fastlyc.v1.views.dog import ns as dog_ns

blueprint = Blueprint("api", __name__)


api = Api(
    blueprint, title="FLASK RESTX API", version="1.0", description="FLASK RESTX API "
)


api.add_namespace(cat_ns, '/cat')
api.add_namespace(dog_ns, '/dog')


@blueprint.before_app_first_request
def before_app_first_request():
    print('app first')


@blueprint.before_request
def before_request():
    print('req first')


'''
捕获HTTPException并转化成指定相应
'''


@blueprint.errorhandler(404)
def not_found(error):
    logger.error(error.description)
    return {'message': str(error.description)}, 404


@blueprint.errorhandler(500)
def not_found(error):
    logger.error(error.description)
    return {'message': str(error.description)}, 500


'''
捕获内部异常并转化成HTTPException
'''


@api.errorhandler(FileNotFoundError)
def no_file(error):
    abort(500, 'no file')


@api.errorhandler(ZeroDivisionError)
def no_file(error):
    abort(500, error)


# 默认处理
@api.errorhandler
def unknown(error):
    abort(500, error)
