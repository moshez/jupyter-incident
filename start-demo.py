cd build/promrun
PYTHONPATH=../../ python -m twisted web --wsgi exporter.application &
../binaries/prometheus-2.22.0.linux-amd64/prometheus --config.file ../prometheus.yml  &
