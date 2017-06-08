# broker_url = 'pyamqp://[USERNAME]:[PASSWORD]@[IP_OR_HOSTNAME]//'
broker_url = 'pyamqp://guest@localhost//'
result_backend = 'rpc://'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json', 'pickle']
# timezone = 'Asia/Taipei'
enable_utc = True
