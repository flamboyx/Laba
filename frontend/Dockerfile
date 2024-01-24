FROM node:lts
LABEL authors="flamboyx"

ARG PROJ_DIR=/frontend

RUN mkdir -p ${PROJ_DIR}

WORKDIR ${PROJ_DIR}

COPY package*.json ${PROJ_DIR}

RUN npm install -g npm
RUN npm install

COPY . ${PROJ_DIR}

RUN chmod +x entry.sh

ENTRYPOINT ["bash", "entry.sh"]