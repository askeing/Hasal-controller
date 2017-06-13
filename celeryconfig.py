# broker_url = 'pyamqp://[USERNAME]:[PASSWORD]@[IP_OR_HOSTNAME]//'
# broker_url = 'pyamqp://guest@localhost//'
broker_url = 'pyamqp://[pulse-username]:[pulse-pwd]@pulse.mozilla.org//'
broker_use_ssl = True
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json', 'pickle']
timezone = 'Asia/Taipei'
enable_utc = True
# task_default_exchange = 'celery'
# task_default_queue = 'celery'
# event_queue_prefix = 'celeryev'
# Ref: https://wiki.mozilla.org/Auto-tools/Projects/Pulse#Security_Model
task_default_exchange = 'exchange/hasal-dev/celery'
task_default_queue = 'queue/hasal-dev/celery'
event_queue_prefix = 'queue/hasal-dev/celeryev'

"""
Celery have to create and access four exchanges:
    celery  direct
    celery.pidbox   fanout
    celeryev        topic
    reply.celery.pidbox     direct

We can modify the settings by task_default_exchange, task_default_queue, event_queue_prefix.
However, celery.pidbox and reply.celery.pidbox cannot be modified.
"""

# Backward Compatible
# Ref: http://docs.celeryproject.org/en/latest/userguide/configuration.html#new-lowercase-settings
BROKER_URL = broker_url
BROKER_USE_SSL = broker_use_ssl
CELERY_RESULT_BACKEND = result_backend

CELERY_TASK_SERIALIZER = task_serializer
CELERY_RESULT_SERIALIZER = result_serializer
CELERY_ACCEPT_CONTENT= accept_content
CELERY_TIMEZONE = timezone
CELERY_ENABLE_UTC = enable_utc
CELERY_DEFAULT_EXCHANGE = task_default_exchange
CELERY_DEFAULT_QUEUE = task_default_queue
CELERY_EVENT_QUEUE_PREFIX = event_queue_prefix
