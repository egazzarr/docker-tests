FROM jupyter/scipy-notebook:python-3.10
LABEL maintainer="Elena Gazzarrini"
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE

RUN pip install --upgrade pip

USER root

# Install ROOT
ENV LANG=C.UTF-8	
ARG ROOT_BIN=root_v6.30.02.Linux-almalinux9.3-x86_64-gcc11.4.tar.gz 

WORKDIR /opt

COPY packages packages

RUN apt-get update -qq \
    && ln -sf /usr/share/zoneinfo/UTC /etc/localtime \
    && apt-get -y install $(cat packages) wget\
    && rm -rf /var/lib/apt/lists/*\
    && wget https://root.cern/download/${ROOT_BIN} \
    && tar -xzvf ${ROOT_BIN} \
    && rm -f ${ROOT_BIN} \
    && echo /opt/root/lib >> /etc/ld.so.conf \
    && ldconfig

ENV ROOTSYS /opt/root
ENV PATH $ROOTSYS/bin:$PATH
ENV PYTHONPATH $ROOTSYS/lib:$PYTHONPATH
ENV CLING_STANDARD_PCH none


# USER $NB_UID

USER root 

RUN conda install -y -c conda-forge python-gfal2 \
    && conda clean --all -f -y

RUN pip install rucio-jupyterlab>=0.9.8 \
    && pip install swanoauthrenew==1.0.1 PyJWT \ 
    && jupyter serverextension enable --py rucio_jupyterlab --sys-prefix \
    && jupyter serverextension enable --py swanoauthrenew --sys-prefix \
    && pip install reana-client>=0.9.0 \
    && pip install ipykernel
    
    
RUN pip install dask && pip install distributed && pip install dask-gateway \
    && pip install jupyter-server-proxy \
    && jupyter serverextension enable --sys-prefix jupyter_server_proxy \
    && pip install dask-labextension 

USER root

RUN apt update -y \
    && apt install -y build-essential curl voms-clients-java software-properties-common \
    && apt clean -y \
    && rm /opt/conda/bin/voms-proxy-init \
    && ln -s /usr/bin/voms-proxy-init /opt/conda/bin/voms-proxy-init

# ESCAPE grid-security and VOMS setup
RUN wget -q -O - https://dist.eugridpma.info/distribution/igtf/current/GPG-KEY-EUGridPMA-RPM-3 | apt-key add -

RUN apt update \
    && add-apt-repository 'deb http://repository.egi.eu/sw/production/cas/1/current egi-igtf core' \
    && apt -y install ca-policy-egi-core

RUN mkdir -p /etc/vomses \
    && wget https://indigo-iam.github.io/escape-docs/voms-config/voms-escape.cloud.cnaf.infn.it.vomses -O /etc/vomses/voms-escape.cloud.cnaf.infn.it.vomses \
    && mkdir -p /etc/grid-security/vomsdir/escape \
    && wget https://indigo-iam.github.io/escape-docs/voms-config/voms-escape.cloud.cnaf.infn.it.lsc -O /etc/grid-security/vomsdir/escape/voms-escape.cloud.cnaf.infn.it.lsc

# Setup merged CERN CA file on Ubuntu based images.
# This file is contained in the `CERN-bundle.pem` file downloaded using 
RUN mkdir /certs \
    && touch /certs/rucio_ca.pem \
    && curl -fsSL 'https://cafiles.cern.ch/cafiles/certificates/CERN%20Root%20Certification%20Authority%202.crt' | openssl x509 -inform DER -out /tmp/cernrootca2.crt \
    && curl -fsSL 'https://cafiles.cern.ch/cafiles/certificates/CERN%20Grid%20Certification%20Authority(1).crt' -o /tmp/cerngridca.crt \
    && curl -fsSL 'https://cafiles.cern.ch/cafiles/certificates/CERN%20Certification%20Authority.crt' -o /tmp/cernca.crt \
    && cat /tmp/cernrootca2.crt >> /certs/rucio_ca.pem \
    && cat /tmp/cerngridca.crt >> /certs/rucio_ca.pem \
    && cat /tmp/cernca.crt >> /certs/rucio_ca.pem \
    && rm /tmp/*.crt \
    && update-ca-certificates

# Setup extension Rucio instance config
ADD configure.py /opt/setup-rucio-jupyterlab/configure.py
ADD setup.sh /usr/local/bin/setup.sh
RUN fix-permissions /opt/setup-rucio-jupyterlab \
    && fix-permissions /usr/local/bin/setup.sh \
    && sed -i -e 's/\r$/\n/' /usr/local/bin/setup.sh \
    && chmod +x /usr/local/bin/setup.sh

RUN mkdir -p /opt/rucio \
    && chown -R $NB_UID /opt/rucio \
    && /usr/local/bin/setup.sh \
    && chown -R $NB_UID /etc/jupyter/jupyter_notebook_config.json \
    && chown -R $NB_UID /etc/jupyter/jupyter_notebook_config.py

ENV IPYTHONDIR=/etc/ipython
ADD ipython_kernel_config.json /etc/ipython/profile_default/ipython_kernel_config.json
RUN chown -R $NB_UID /etc/ipython
ENV JUPYTER_ENABLE_LAB=yes

WORKDIR $HOME
USER $NB_UID

CMD ["setup.sh", "start-notebook.sh"]
