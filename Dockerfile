# ARG BASETAG=0.9.1-alpha.3
 
# # To be changed to specific version+hsa
# FROM reanahub/reana-server:${BASETAG}
# LABEL maintainer="E. Gazzarrini"

# # Workdir is /home
# COPY requirements.txt iam_email.py iam.ini /home/

# RUN pip install -r /home/requirements.txt

# # install kubectl 
# RUN apt-get update && apt-get install -y kubectl

# # ENTRYPOINT ["/bin/bash"]

# This file is part of REANA.
# Copyright (C) 2017, 2018, 2019, 2020, 2021, 2022, 2023 CERN.
#
# REANA is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

# Use Ubuntu LTS base image
FROM docker.io/library/ubuntu:20.04

# Use default answers in installation commands
ENV DEBIAN_FRONTEND=noninteractive

# Prepare list of Python dependencies
COPY requirements.txt /code/

# Install all system and Python dependencies in one go
# hadolint ignore=DL3008, DL3013
RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
      gcc \
      git \
      vim-tiny \
      libffi-dev \
      procps \
      kubectl \
      libpython3.8 \
      python3.8 \
      python3.8-dev \
      python3-pip && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /code/requirements.txt && \
    apt-get remove -y \
      gcc \
      python3.8-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

# Copy cluster component source code
WORKDIR /code
COPY . /code

# Are we debugging?
ARG DEBUG=0
RUN if [ "${DEBUG}" -gt 0 ]; then pip install -e ".[debug]"; else pip install .; fi;

# Are we building with locally-checked-out shared modules?
# hadolint ignore=SC2102
RUN if test -e modules/reana-commons; then pip install -e modules/reana-commons[kubernetes,yadage,snakemake,cwl] --upgrade; fi
RUN if test -e modules/reana-db; then pip install -e modules/reana-db --upgrade; fi

# A quick fix to allow eduGAIN and social login users that wouldn't otherwise match Invenio username rules
RUN sed -i 's|^username_regex = re.compile\(.*\)$|username_regex = re.compile("^\\S+$")|g' /usr/local/lib/python3.8/dist-packages/invenio_userprofiles/validators.py

# Check for any broken Python dependencies
RUN pip check

# Set useful environment variables
ENV TERM=xterm \
    FLASK_APP=/code/reana_server/app.py

# Expose ports to clients
EXPOSE 5000

# Run server
CMD ["uwsgi --ini uwsgi.ini"]

