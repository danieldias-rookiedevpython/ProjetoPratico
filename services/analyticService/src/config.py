from os import getenv


PROMETHEUS_URL = getenv("PROMETHEUS_URL", "http://prometheus:9090")
