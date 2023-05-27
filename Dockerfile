FROM python:3.11.3-bullseye
COPY pyproject.toml poetry.lock /app/
WORKDIR /app
RUN apt-get update && \
    apt install -y ffmpeg git curl gcc musl-dev &&  \
    pip install --no-cache-dir poetry==1.4.2 && \
    poetry config virtualenvs.create false --local && \
    poetry install && \
    pip uninstall -y poetry && \
    apt remove -y git curl gcc musl-dev && \
    rm -rf /root/.cache/ && \
    rm -rf /usr/local/src/*
RUN mkdir -p /root/.cache/whisper
RUN wget https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt -O /root/.cache/whisper/medium.pt
COPY app.py /app
ENTRYPOINT ["python3", "app.py"]
