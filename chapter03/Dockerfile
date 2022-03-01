# Define custom function directory
ARG FUNCTION_DIR="/function"

FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.8.1-cpu-py36-ubuntu18.04 as build-image

ARG FUNCTION_DIR

RUN apt-get update && \
  apt-get install -y \
  g++ \
  make \
  cmake \
  unzip \
  libcurl4-openssl-dev

RUN mkdir -p ${FUNCTION_DIR}
COPY app/ ${FUNCTION_DIR}/


RUN pip install \
    --target ${FUNCTION_DIR} \
        awslambdaric


FROM 763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-inference:1.8.1-cpu-py36-ubuntu18.04

ARG FUNCTION_DIR
WORKDIR ${FUNCTION_DIR}
COPY --from=build-image ${FUNCTION_DIR} ${FUNCTION_DIR}

ENTRYPOINT [ "/opt/conda/bin/python", "-m", "awslambdaric" ]
CMD [ "app.handler" ]