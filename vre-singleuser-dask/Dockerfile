FROM ghcr.io/vre-hub/vre-singleuser:sha-40199b2
LABEL maintainer="VRE Team @ CERN 22/23 - E. Garcia, E. Gazzarrini, D. Gosein"
LABEL org.opencontainers.image.source https://github.com/vre-hub/environments
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE

# WORKDIR $HOME
USER $NB_UID

# RUN pip install bokeh==3.2.2 \
#     && pip install dask==2023.9.2 \
#     && pip install dask-gateway==2023.1.1 \
#     && pip install dask-labextension==7.0.0

RUN pip install dask>=2023.5.1 \
    && pip install distributed>=2023.5.1 \
    && pip install dask-gateway>=2022.4.0 \
    && pip install bokeh>=3.0.0 \
    && pip install jupyter-server-proxy \
    && jupyter serverextension enable --sys-prefix jupyter_server_proxy
    # && pip install dask-labextension>=6.1.0
