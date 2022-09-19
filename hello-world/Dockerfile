ARG PYTHON_VERSION=3.9
FROM python:$PYTHON_VERSION-slim as builder

ENV PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt .
RUN pip install -r requirements.txt --prefix=/install

FROM python:$PYTHON_VERSION-slim

RUN useradd app -d /app
WORKDIR /app

COPY main.py /app
USER app
COPY --from=builder /install /usr/local

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
