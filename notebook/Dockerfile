FROM jupyter/base-notebook

# Declare environmental variables

ARG PG_DB
ARG PG_HOST
ARG PG_USER
ARG PG_PW
ARG JUPYTER_TOKEN
ARG DOCKER_STACKS_JUPYTER_CMD
ENV PG_DB ${PG_DB}
ENV PG_HOST ${PG_HOST}
ENV PG_USER ${PG_USER}
ENV PG_PW ${PG_PW}
ENV JUPYTER_TOKEN ${JUPYTER_TOKEN}
ENV DOCKER_STACKS_JUPYTER_CMD ${DOCKER_STACKS_JUPYTER_CMD}

COPY ./notebooks /home/jovyan/
USER root
# Install in the default python3 environment
RUN pip install --no-cache-dir 'flake8' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install from the requirements.txt file
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir --requirement /tmp/requirements.txt && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
USER jovyan