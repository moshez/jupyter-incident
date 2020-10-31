from prometheus_client import CollectorRegistry, Gauge
from pyramid.config import Configurator
from pyramid.response import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
import itertools
import random

LEVELS = {
   "object1": itertools.cycle([2, 2, 3, 4, 2, 2]),
   "object2": itertools.cycle([20, 24, 23, 20, 22, 20]),
   "object2": itertools.cycle([10, 12, 13, 14, 12, 12]),
   "object4": itertools.cycle([10, 22, 3, 24, 12, 12]),
   "object5": itertools.cycle([2, 3, 5, 4, 9, 2]),
}

def measure():
    registry = CollectorRegistry()
    g = Gauge(
         "level",
         "Level",
         ["which"],
         registry=registry
    )
    for key, value in LEVELS.items():
       g.labels(key).set(next(value) + random.uniform(-3, 3))
    return registry

def metrics_web(request):
    registry = measure()
    return Response(generate_latest(registry),
                    content_type=CONTENT_TYPE_LATEST)

with Configurator() as config:
    config.add_route('metrics', '/metrics')
    config.add_view(metrics_web, route_name='metrics')
    application = config.make_wsgi_app()
