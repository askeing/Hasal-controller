# Server Installation

## RabbitMQ

See [Installing RabbitMQ](http://www.rabbitmq.com/install-debian.html).

Or you can install it by `apt`.

```bash
$ sudo apt install rabbitmq-server
```

## Celery and flower

Install `Celery` and `flower`

```bash
$ pip install -r requirements.txt
```

## Running flower

Running `flower` on port 5555.

```bash
$ celery flower -A tasks --port=5555
```

Then open browser and access `http://localhost:5555/`.

# Worker Installation

## Celery

You can install `Celery` by pip.

We will suggest you install it in `vitrualenv`.

```bash
$ pip install celery
```

## Running Worker
```bash
$ celery -A tasks worker -c 1 --loglevel=info
```

# Boss Installation

## Celery

You can install `Celery` by pip.

We will suggest you install it in `vitrualenv`.

```bash
$ pip install celery
```
## Running Boss to trigger Periodic Tasks

```bash
$ celery beat --conf celeryconfig
```

# Demo

There is a simple demo code `driver.py`.

You can test it after starting the `worker` and `flower`.

```bash
$ python driver.py
```

You should get the following output:
```bash
### add 1, 5
Return:
6
### add job: {'platform': 'linux32', 'tests': ['test_firefox_testsuite_foo', 'test_firefox_testsuite_bar'], 'max_run': 30, 'suitename': 'try test suite'}
Return:
{"platform": "linux32", "tests": {"test_firefox_testsuite_bar": {"values": {"si": 200, "runtime_average": 10, "psi": 250, "runtime_median": 12}, "name": "test_firefox_testsuite_bar"}, "test_firefox_testsuite_foo": {"values": {"si": 200, "runtime_average": 10, "psi": 250, "runtime_median": 12}, "name": "test_firefox_testsuite_foo"}}, "max_run": 30, "suitename": "try test suite"}
```
