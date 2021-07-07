FROM python:3.7-slim

ADD . /resqs/
ENV PYTHONUNBUFFERED 1

WORKDIR /resqs/
RUN  pip3 --no-cache-dir install --upgrade pip setuptools && \
     pip3 --no-cache-dir install ".[server]"

ENTRYPOINT ["/usr/local/bin/moto_server", "-H", "0.0.0.0"]

EXPOSE 5000
