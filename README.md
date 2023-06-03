# Netflux ESIR - Lang-Indent

This repository contains the lang-indent of the Netflux ESIR project used to identify the language of a video 
and to generate subtitles.

## Install

### Requirements

- [Python](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [poetry](https://python-poetry.org/docs/#installation)
- [ffmpeg](https://ffmpeg.org/download.html)
- [Docker](https://docs.docker.com/get-docker/) (optional)
- [Docker Compose](https://docs.docker.com/compose/install/) (optional)

### Run from source

```bash
git clone https://github.com/NetfluxESIR/lang-indent.git
cd lang-indent
poetry install
poetry run python app.py [command]
```

### Run with Docker

```bash
docker run ghcr.io/netfluxesir/lang-indent:latest [command]
```

> Note: you can also use the [docker-compose.yml](./docker-compose.yaml) file to run the lang-indent locally.

