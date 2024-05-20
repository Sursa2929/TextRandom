FROM python:3.11.7-alpine3.17

WORKDIR /app

COPY . .
RUN apk add --no-cache gcc libffi-dev musl-dev ffmpeg aria2 && pip install --upgrade pip --no-cache-dir -r requirements.txt

CMD [ "python", "Surya/main.py" ]
