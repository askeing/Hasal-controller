import tasks

# calling the add() method, and then get the result
print('### add 1, 5')
add_task = tasks.add.delay(1, 5)    # this method will sleep 10 sec
add_ret = add_task.get(timeout=20)
print('Return:')
print(add_ret)


# calling the add_job() method
fake_input_data = {
    'suitename': 'try test suite',
    'platform': 'linux32',
    'max_run': 30,
    'tests': [
        'test_firefox_testsuite_foo',
        'test_firefox_testsuite_bar'
    ]
}
print('### add job: {}'.format(fake_input_data))
addjob_task = tasks.add_job.delay(fake_input_data)
addjob_ret = addjob_task.get()
print('Return:')
print(addjob_ret)
