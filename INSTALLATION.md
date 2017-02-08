# Boss Installation

## Celery

You can install `Celery` by pip.

We will suggest you install it in `vitrualenv`.

```bash
$ pip install celery
```
## Run Boss for triggering jobs

```bash
$ celery beat --conf celeryconfig
```

# Worker Installation

## Celery

You can install `Celery` by pip.

We will suggest you install it in `vitrualenv`.

```bash
$ pip install celery
```

## Run Worker
```bash
$ celery -A tasks worker -c 1 --loglevel=info
```

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
