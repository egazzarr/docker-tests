ARG BASETAG=2023.8.1-py3.9
# ARG BASETAG=2023.2.1-py3.8
 
# To be changed to specific version+hsa
FROM ghcr.io/dask/dask-notebook:${BASETAG}
LABEL maintainer="E. Gazzarrini"

ENV LANG=C.UTF-8

ARG ROOT_BIN=root_v6.28.06.Linux-ubuntu22-x86_64-gcc11.4.tar.gz

WORKDIR /opt

COPY packages packages
COPY requirements.txt /opt

# Necessary to switch temporarily to root user from the default user of Pangeo
# image
USER root
RUN apt-get update -qq \
 && ln -sf /usr/share/zoneinfo/UTC /etc/localtime \
 && apt-get -y --no-install-recommends install $(cat packages) wget\
 && rm -rf /var/lib/apt/lists/*\
 && wget https://root.cern/download/${ROOT_BIN} \
 && tar -xzvf ${ROOT_BIN} \
 && rm -f ${ROOT_BIN} \
 && echo /opt/root/lib >> /etc/ld.so.conf \
 && ldconfig

RUN pip install -r /opt/requirements.txt

# Switch back to default user
USER 1000

ENV ROOTSYS /opt/root
ENV PATH $ROOTSYS/bin:$PATH
ENV PYTHONPATH $ROOTSYS/lib:$PYTHONPATH
ENV CLING_STANDARD_PCH none

CMD ["root", "-b"]


 
 

 
