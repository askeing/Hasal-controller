from celery.schedules import crontab

# trigger the scheduled tasks: $ celery beat --conf celeryconfig
# or running worker with --beat parameter for single worker.
beat_schedule = {
    'every-hour': {
        'task': 'tasks.add',
        'schedule': crontab(minute=0, hour='*'),
        'args': (1, 3)
    },
    'every-min': {
        'task': 'tasks.add_job',
        'schedule': crontab(),
        'kwargs': {
            'data': {
                'suitename': 'try test suite',
                'platform': 'linux32',
                'max_run': 30,
                'tests': [
                    'test_firefox_testsuite_foo',
                    'test_firefox_testsuite_bar'
                ]
            }
        }
    }
}

