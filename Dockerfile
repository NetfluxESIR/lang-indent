FROM python:3.11.3-alpine3.17 as base
COPY pyproject.toml /app/
WORKDIR /app
RUN pip install poetry
RUN poetry export --without-hashes -f requirements.txt -o requirements.txt

FROM python:3.11.3-alpine3.17 as final
COPY . /app
COPY --from=base /app/requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py", "run"]
