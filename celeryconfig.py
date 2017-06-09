# broker_url = 'pyamqp://[USERNAME]:[PASSWORD]@[IP_OR_HOSTNAME]//'
broker_url = 'pyamqp://guest@localhost//'
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
