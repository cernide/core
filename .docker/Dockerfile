FROM polyaxon-base-dev

# This dockerfile is intended for dev only purposes
LABEL maintainer="Polyaxon, Inc. <contact@polyaxon.com>"

RUN apt-get -y update && \
    apt-get -y install nginx && \
    apt-get -y install socat && \
    apt-get -y autoremove && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*

COPY /core/requirements /requirements/
RUN pip3 install --no-cache-dir -r /requirements/requirements.txt
RUN pip3 install --no-cache-dir -r /requirements/platform.txt
RUN pip3 install --no-cache-dir -r /requirements/streams.txt
RUN pip3 install --no-cache-dir -r /requirements/prod.txt

ENV PYTHONPATH="${PYTHONPATH}:/core/core"

VOLUME /core
WORKDIR /core
