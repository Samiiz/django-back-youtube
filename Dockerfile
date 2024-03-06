FROM python:3.11
LABEL maintainer='Samiiz'

ENV PYTHONUNBUFFERED 1

# mv랑 비슷함
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# 작업시 /app 이 자동으로 붙는다
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    apt-get update && \
    apt-get install -y postgresql-client build-essential libpq-dev zlib1g zlib1g-dev && \
    if [ "$DEV" = "true" ]; \
        then echo "===THIS IS DEVELOPMENT BUILD===" && \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    apt-get remove -y --purge build-essential libpq-dev && \
    apt-get clean && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /vol/web && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web && \
    chmod -R +x /scripts 

ENV PATH="/scripts:/py/bin/:$PATH"

USER django-user

CMD ["run.sh"]
