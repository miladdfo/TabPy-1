# docker build -t tabpy-dfo .
# docker run -it -p 9004:9004 tabpy-dfo:latest
# Build tabpy image
FROM continuumio/miniconda3:latest

# AWS and SSH keys
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG SSH_PRIVATE
ARG SSH_PUBLIC

# Install zip
RUN apt-get update && apt-get install -y zip

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$SSH_PRIVATE" > /root/.ssh/id_rsa && \
    echo "$SSH_PUBLIC" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

# Install python dependencies
RUN pip install xgboost pandas sklearn scipy matplotlib

# Install aws-cli
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
                unzip awscli-bundle.zip && \
                ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
                rm awscli-bundle.zip && rm -rf awscli-bundle

# Pull down python script to build model
RUN git clone git@github.com:DFOGlobalPerformanceCommerce/fraud-model.git
WORKDIR fraud-model
RUN mkdir data
WORKDIR data

# Download datasets
RUN /usr/local/bin/aws s3 cp s3://dfo-datasets/fraud-data/full_fraud_data.csv .
RUN /usr/local/bin/aws s3 cp s3://dfo-datasets/fraud-data/different_addresses_data.csv .

WORKDIR /

ENV key=value
ENV key2=value
ENV key3=value
ENV key4=value
ARG CACHE_DATE=2016-01-05
# Install TabPy and run server
RUN git clone git@github.com:miladdfo/TabPy-1.git
WORKDIR TabPy-1/tabpy-server
RUN python setup.py install


# Add and run startup script
WORKDIR /TabPy-1/tabpy-server/tabpy_server
ENTRYPOINT ["bash", "startup.sh"]
