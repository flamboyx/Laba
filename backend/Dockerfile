FROM python:3.12
LABEL authors="flamboyx"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJ_DIR=/backend

RUN mkdir -p ${PROJ_DIR}
COPY . ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

RUN pip install --upgrade pip \
    pip install -r requirements.txt

RUN chmod +x entry.sh

ENTRYPOINT ["bash", "entry.sh"]