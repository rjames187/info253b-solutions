FROM python:3.9-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["rq"]
CMD ["worker", "-u", "redis://broker:6379"]