import os
import json
import logging

logger = logging.getLogger(__file__)

"""
Loading Broker URL
"""

"""
# RabbitMQ Broker
broker_url = 'pyamqp://guest@localhost//'

BROKER_URL_FMT = 'pyamqp://{username}:{password}@{host}//'
LC_CELERY_USERNAME = 'celery_username'
LC_CELERY_PASSWORD = 'celery_password'
LC_CELERY_HOST = 'celery_host'
LC_CHECK_LIST = [LC_CELERY_USERNAME, LC_CELERY_PASSWORD, LC_CELERY_HOST]

current_dir = os.path.dirname(__file__)
config_json_name = 'celery-config.json'
config_json_file = os.path.join(current_dir, config_json_name)
if os.path.exists(config_json_file):
    try:
        with open(config_json_file, 'r') as config_fh:
            config_json = json.load(config_fh)

        # checking the required information from config file
        check_pass = reduce((lambda x, y: x and y), [item in config_json for item in LC_CHECK_LIST])
        if check_pass:
            broker_url = BROKER_URL_FMT.format(username=config_json.get(LC_CELERY_USERNAME),
                                               password=config_json.get(LC_CELERY_PASSWORD),
                                               host=config_json.get(LC_CELERY_HOST))
    except Exception as e:
        logger.warn('Cannot load JSON file: {f}'.format(f=config_json_file))
"""

# Redis Broker
broker_url = 'redis://:<PASSWORD>@10.247.120.27:6379/0'


"""
Other settings
"""
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json', 'pickle']
timezone = 'Asia/Taipei'
enable_utc = True

# Backward Compatible
# Ref: http://docs.celeryproject.org/en/latest/userguide/configuration.html#new-lowercase-settings
BROKER_URL = broker_url
CELERY_RESULT_BACKEND = result_backend

CELERY_TASK_SERIALIZER = task_serializer
CELERY_RESULT_SERIALIZER = result_serializer
CELERY_ACCEPT_CONTENT= accept_content
CELERY_TIMEZONE = timezone
CELERY_ENABLE_UTC = enable_utc
