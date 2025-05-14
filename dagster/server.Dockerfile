FROM python:3.12-slim

RUN pip install \
  dagster \
  dagster-postgres \
  dagster-k8s 

ARG DAGSTER_GRPC_PORT=4000
ARG DAGSTER_FOLDER="/opt/dagster"

ENV DAGSTER_GRPC_PORT=${DAGSTER_GRPC_PORT}
ENV DAGSTER_FOLDER="${DAGSTER_FOLDER}"
ENV DAGSTER_APP="${DAGSTER_FOLDER}/app"
ENV DAGSTER_HOME="${DAGSTER_FOLDER}/dagster_home"

RUN mkdir -p ${DAGSTER_APP}
RUN mkdir -p ${DAGSTER_HOME}

COPY dagster.yaml ${DAGSTER_HOME}

WORKDIR ${DAGSTER_APP}

# grpc expose port
EXPOSE ${DAGSTER_GRPC_PORT}

ENTRYPOINT dagster code-server start -h 0.0.0.0 -p ${DAGSTER_GRPC_PORT} -m defs