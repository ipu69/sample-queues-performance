# Builder image: install requirements
FROM python:3.8-alpine AS build

LABEL maintainer="Andrey Larionov <larioandr@gmail.com>"
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add gcc python3-dev musl-dev
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


# Test image: run flake8 and pytest
FROM python:3.8-alpine AS test

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flake8 pytest
RUN mkdir /wheels

COPY --from=build /wheels /wheels
# For some reason, GitHub actions require this between successive COPY --from=... commands: 
# https://github.community/t5/GitHub-Actions/Attempting-to-build-docker-image-with-COPY-from-on-Actions/td-p/36445
RUN true
COPY --from=build /app/requirements.txt .
RUN ls -1A /wheels | grep -q . && pip install --no-cache /wheels/* || echo 'no wheels found'

COPY model.py .
RUN flake8 model.py

COPY model_test.py .
RUN pytest model_test.py


# Final image: copy model.py from test and launch it
FROM python:3.8-alpine

WORKDIR /app

RUN pip install --upgrade pip

COPY --from=build /wheels /wheels
# Once more, just for GitHub actions to work (see above):
RUN true 
COPY --from=build /app/requirements.txt .
RUN ls -1A /wheels | grep -q . && pip install --no-cache /wheels/* || echo 'no wheels found'

COPY --from=test /app/model.py .

ENTRYPOINT ["python", "/app/model.py"]
