FROM python:3.12-slim

RUN pip install \
  dagster \
  dagster-graphql \
  dagster-webserver \
  dagster-postgres

ARG DAGSTER_WEB_PORT=3000
ENV DAGSTER_WEB_PORT=${DAGSTER_WEB_PORT}
ENV DAGSTER_HOME=/opt/dagster/dagster_home/

RUN mkdir -p ${DAGSTER_HOME}
COPY workspace.yaml dagster.yaml ${DAGSTER_HOME}

WORKDIR ${DAGSTER_HOME}

EXPOSE ${DAGSTER_WEB_PORT}

ENTRYPOINT dagster-webserver -h 0.0.0.0 -p ${DAGSTER_WEB_PORT} -w workspace.yaml