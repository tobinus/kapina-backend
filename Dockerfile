FROM alpine:3.7 as base

WORKDIR /srv/app

RUN apk add --update --no-cache git gcc libc-dev python3 python3-dev jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

COPY requirements.txt .
RUN pip3 --no-cache-dir install -r requirements.txt

FROM alpine:3.7 as production

WORKDIR /srv/app
COPY --from=base /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages 
RUN apk add --update --no-cache uwsgi-python3
