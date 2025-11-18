FROM python:3.12-slim
WORKDIR /app

ENV FLASK_APP=app.py \
    FLASK_RUN_HOST=0.0.0.0 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y  --no-install-recommends \
   build-essential \
   && rm -r /var/lib/apt/lists*
# COPY requirements.txt app/requirements.txt
COPY . .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --root-user-action=ignore -r requirements.txt
EXPOSE 5000


RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

# CMD ["flask", "run", "--debug"]
