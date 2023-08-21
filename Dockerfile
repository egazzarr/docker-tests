ARG BASETAG=0.9.1-alpha.3
 
# To be changed to specific version+hsa
FROM reanahub/reana-server:${BASETAG}
LABEL maintainer="E. Gazzarrini"

# Workdir is /home
COPY requirements.txt iam_email.py iam.ini /home/

RUN pip install -r /home/requirements.txt

ENTRYPOINT ["/bin/bash"]

