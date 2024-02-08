# version
FROM python:3.11.6
ENV PYTHONBUFFERED=1

# env
ENV APP=myapp

# work dir
WORKDIR /${APP}

# copy
RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

# confirm if that is needed
COPY . /${APP}/