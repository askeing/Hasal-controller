from __future__ import print_function
import time
import json
import base64
import subprocess

from celery import Celery


app = Celery('tasks')
app.config_from_object('celeryconfig')

app.control.mailbox.exchange_fmt = 'exchange/hasal-dev/%s.pidbox'
app.control.mailbox.reply_exchange_fmt = 'exchange/hasal-dev/reply.%s.pidbox'

# exchange_fmt = '%s.pidbox'
# reply_exchange_fmt = 'reply.%s.pidbox'


@app.task
def add(x, y):
    time.sleep(10)
    return x + y


@app.task
def add_job(data):
    """
    :param data: dict object with 'x' and 'y'.
    :return: the sum of 'x' and 'y'
    """
    if 'suitename' in data:
        suitename = data.get('suitename')
        platform = data.get('platform')
        max_run = data.get('max_run')
        tests = data.get('tests', [])
        print('### {0} Got ###'
              'Platform {1}, max_run {2}.'
              'tests: {3}'.format(suitename, platform, max_run, tests))

        tests_result = {}
        for test in tests:
            test_ret = {
                'name': test,
                'values': {
                    'runtime_median': 12,
                    'runtime_average': 10,
                    'si': 200,
                    'psi': 250
                }
            }
            tests_result[test] = test_ret

        for idx in range(10):
            print('{}%'.format((idx+1)*10))
            time.sleep(1)

        result = {
            'suitename': suitename,
            'platform': platform,
            'max_run': max_run,
            'tests': tests_result
        }
        try:
            result_json = json.dumps(result)
            print('### {0} Finished ###'.format(suitename))
            return result_json
        except:
            print('### {0} Failed ###'.format(suitename))
            return ''


@app.task
def get_file():
    with open('img.png', 'r') as f:
        encoded_data = base64.b64encode(f.read())
        return encoded_data


@app.task
def run_hasal():
    command_list = ['python', 'runtest.py']
    print('### Run command: {}'.format(' '.join(command_list)))
    subprocess.call(command_list)


def save_file(encoded_data):
    with open('img2.png', 'w') as fw:
        decoded_data = base64.b64decode(encoded_data)
        fw.write(decoded_data)
