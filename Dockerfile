FROM python:3.6-alpine

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]
