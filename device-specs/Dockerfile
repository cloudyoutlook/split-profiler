FROM ubuntu:20.04

ARG DEBIAN_FRONTEND="noninteractive"
ENV TZ="Europe/London"

RUN apt-get update -y \
    && apt install python3 -y \
    && apt install python3-pip -y \
    && apt install python3-venv -y \
    && python3 -m venv venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY go.robot /opt/app/go.robot

CMD ["robot", "-d", "/opt/app/", "/opt/app/go.robot"]

