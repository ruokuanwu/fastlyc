import datetime
import logging
import logging.handlers
import pathlib
# from flask_jwt_extended import JWTManager,create_access_token

from config import helper_config

# 日志处理

logger = logging.Logger('apiv1', logging.DEBUG)

p = pathlib.Path(helper_config.get(
    'fastlyc_v1_log_file_path', 'logs/apiv1.log'))
if not p.parent.exists():
    p.parent.mkdir()

handler = logging.handlers.TimedRotatingFileHandler(
    p.absolute(), when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))

handler.setFormatter(logging.Formatter(
    "[%(asctime)s %(levelname)s] %(message)s"))

logger.addHandler(handler)

# jwt认证
# jwt=JWTManager()
