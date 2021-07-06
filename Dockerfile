FROM python:3.7-slim

ADD . /rescue_moto/
ENV PYTHONUNBUFFERED 1

WORKDIR /rescue_moto/
RUN  pip3 --no-cache-dir install --upgrade pip setuptools && \
     pip3 --no-cache-dir install ".[server]"

ENTRYPOINT ["/usr/local/bin/moto_server", "-H", "0.0.0.0"]

EXPOSE 5000
