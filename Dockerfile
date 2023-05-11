FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ARG ENVIRONMENT
ENV ENV=${ENVIRONMENT}

RUN if [ "$ENVIRONMENT" = "develop" ] || [ "$ENVIRONMENT" = "debug" ]; then \
      apt update ; \
      apt install -y npm ; \
      npm i -g nodemon ; \
    fi

ENV PYTHONUNBUFFERED=1
