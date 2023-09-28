FROM ghcr.io/vre-hub/vre-singleuser:sha-40199b2
LABEL maintainer="VRE Team @ CERN 22/23 - E. Garcia, E. Gazzarrini, D. Gosein"
LABEL org.opencontainers.image.source https://github.com/vre-hub/environments
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE

USER $NB_UID

RUN pip install bokeh==3.2.2 \
    && pip install dask==2023.9.2 \
    && pip install dask-gateway==2023.1.1 \
    && pip install dask-labextension==7.0.0