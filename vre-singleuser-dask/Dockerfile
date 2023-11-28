FROM ghcr.io/vre-hub/vre-singleuser:sha-423e01a
LABEL maintainer="VRE Team @ CERN 22/23 - E. Garcia, E. Gazzarrini, D. Gosein"
LABEL org.opencontainers.image.source https://github.com/vre-hub/environments
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE

WORKDIR $HOME
USER root
USER $NB_UID
# COPY --chown=1000:100 ./ /home/$NB_USER/

# RUN pip install bokeh==3.2.2 \
#     && pip install dask==2023.9.2 \
#     && pip install dask-gateway==2023.1.1 \
#     && pip install dask-labextension==7.0.0

RUN pip install dask>=2023.5.1 \
    && pip install distributed>=2023.5.1 \
    && pip install dask-gateway>=2022.4.0 \
    && pip install jupyter-server-proxy \
    && jupyter serverextension enable --sys-prefix jupyter_server_proxy \
    && pip install dask-labextension==6.2.0 \
    && pip uninstall -y bokeh 
    
RUN pip install --upgrade pip
RUN pip install bokeh>=2.4.2,<3
    

WORKDIR $HOME
USER $NB_UID

CMD ["setup.sh", "start-notebook.sh"]
