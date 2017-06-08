from celery.schedules import crontab

# trigger the scheduled tasks: $ celery beat --conf celeryconfig-boss
# or running worker with --beat parameter for single worker.
beat_schedule = {
    'every-hour': {
        'task': 'tasks.add_job',
        'schedule': crontab(minute=0, hour='*'),
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

