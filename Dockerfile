ARG BASETAG=0.9.1-alpha.3
 
# To be changed to specific version+hsa
FROM reanahub/reana-server:${BASETAG}
LABEL maintainer="VRE Team @ CERN 22/23 - E. Garcia, E. Gazzarrini, D. Gosein"
LABEL org.opencontainers.image.source https://github.com/vre-hub/vre
ARG BUILD_DATE
LABEL org.label-schema.build-date=$BUILD_DATE

# Workdir is /home
COPY requirements.txt iam_email.py iam.ini /home/

RUN pip install -r /home/requirements.txt

ENTRYPOINT ["/bin/bash"]

