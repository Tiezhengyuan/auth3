# version
FROM python:3.11.6

# env
ENV APP=myapp

# work dir
WORKDIR /${APP}

# copy
RUN pip install --upgrade pip
COPY requirements.txt /${APP}/
RUN pip install -r requirements.txt

COPY . /${APP}/