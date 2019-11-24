"""Gunicorn (http server) configuration.
"""

workers = 1
worker_class = 'gthread'
threads = 5
timeout = 60
