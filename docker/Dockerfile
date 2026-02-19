
FROM python:3.10
# Install dependencies from local dist directory using temporary mount.
RUN --mount=type=bind,source=./dist,target=/tmp/offline_dist     pip install --no-build-isolation --no-index --find-links=/tmp/offline_dist/download -r /tmp/offline_dist/requirements.txt &&     pip install --no-build-isolation --no-index --find-links=/tmp/offline_dist/download exemplar_flask==0.0.1
