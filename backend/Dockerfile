FROM python:3.11
LABEL authors="flamboyx"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/backend

RUN mkdir -p ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

COPY requirements.txt ${PROJ_DIR}

RUN pip install --upgrade pip \
    pip install -r requirements.txt

COPY . ${PROJ_DIR}

RUN chmod +x entry.sh

ENTRYPOINT ["bash", "entry.sh"]