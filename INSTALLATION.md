# Server Installation

## RabbitMQ

See [Installing RabbitMQ](http://www.rabbitmq.com/install-debian.html).

Or you can install it by `apt`.

```bash
$ sudo apt install rabbitmq-server
```

### Setting the RabbitMQ Configuration

Creating the [RabbitMQ Configuration](http://www.rabbitmq.com/configure.html#configuration-file) file under `/etc/rabbitmq/rabbitmq.config`:

```bash
$ sudo nano /etc/rabbitmq/rabbitmq.config
```

A simple example (standard Erlang configuration):
```
[
    {rabbit, [{tcp_listeners, [5672]}]}
].
```

### Enabling the Management Plugin

Enable the RabbitMQ's [Management Plugin](https://www.rabbitmq.com/management.html).

```bash
$ sudo rabbitmq-plugins enable rabbitmq_management
```

Then you can access the `http://localhost:15672/` to get the Management Console.

Before you create the admin account, you can only login with `guest/guest` on `localhost` domain.

### Adding User

Clicking `Admin` tab, and then clicking `Add a user` to add a new user.
For example, adding `tester` with password `HASALtest!`.

After creating user, clicking user name `tester`, setting the permission.

### Stop and Start RabbitMQ

To stop RabbitMQ, you can use the [rabbitmqctl](https://www.rabbitmq.com/man/rabbitmqctl.1.man.html).
The following command will instructs the RabbitMQ node to terminate:

```bash
sudo rabbitmqctl stop
```
To start RabbitMQ, you can use `service` (Ubuntu) command:

```bash
sudo service rabbitmq-server start
```

## Celery and flower

Install `Celery` and `flower`

```bash
$ pip install -r requirements-flower.txt
```

### Editing the `celeryconfig` for Celery `tasks`

Modifying the `broker_url` to fit the username, password, and IP address of your **RabbitMQ**.

```python
broker_url = 'pyamqp://[USERNAME]:[PASSWORD]@[IP_OR_HOSTNAME]//'
```

For example:

```python
broker_url = 'pyamqp://tester:HASALtest!@127.0.0.1//'
```

### Running flower

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

### Editing the `celeryconfig` for Celery `tasks`

Modifying the `broker_url` to fit the username, password, and IP address of your **RabbitMQ**.

```python
broker_url = 'pyamqp://[USERNAME]:[PASSWORD]@[IP_OR_HOSTNAME]//'
```

## Running Worker
```bash
$ celery -A tasks worker -c 1 --loglevel=info
```

# Boss Installation

This part is used for running tasks regularly.

## Celery

You can install `Celery` by pip.

We will suggest you install it in `vitrualenv`.

```bash
$ pip install celery
```
## Running Boss to trigger Periodic Tasks

```bash
$ celery beat --conf celeryconfig-boss
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
