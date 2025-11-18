FROM python:3.13-alpine
WORKDIR /app

ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
# COPY requirements.txt app/requirements.txt
COPY . .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
EXPOSE 5000


RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD ["flask", "run", "--debug"]
