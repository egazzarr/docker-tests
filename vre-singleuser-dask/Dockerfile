FROM ghcr.io/vre-hub/vre-singleuser:sha-40199b2
LABEL maintainer="VRE Team @ CERN 22/23 - E. Garcia, E. Gazzarrini, D. Gosein"
LABEL org.opencontainers.image.source https://github.com/vre-hub/environments
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE


RUN git clone https://github.com/egazzarr/docker-tests/vre-singleuser-dask/ \
    && cd ${HOME}/vre-singleuser-dask/ \
    && pip install --no-cache -r requirements.txt 