ARG BASETAG=0.9.1-alpha.3
 
# To be changed to specific version+hsa
FROM reanahub/reana-server:${BASETAG}
LABEL maintainer="E. Gazzarrini"

# Workdir is /home
COPY requirements.txt iam_email.py iam.ini /home/

RUN pip install -r /home/requirements.txt

# install kubectl 
RUN curl -o /usr/bin/kubectl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x /usr/bin/kubectl

ENTRYPOINT ["/bin/bash"]

