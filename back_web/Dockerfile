# version
FROM --platform=linux/amd64 python:3.11.6
ENV PYTHONBUFFERED=1
RUN apt-get update && apt-get install -y iputils.ping

# install
WORKDIR /myapp
COPY requirements.txt /myapp/
RUN pip install -r requirements.txt
COPY ./back_web/ /myapp/


