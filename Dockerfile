FROM amazonlinux:latest

MAINTAINER Yash Indane

EXPOSE 1453

COPY . /

RUN yum install python3 -y && \
    yum install awscli -y && \
    pip3 install -r requirements.txt

WORKDIR /

ENTRYPOINT ["python3", "app2.py"] 
     
