FROM python:3.7

WORKDIR /app
COPY src .
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
