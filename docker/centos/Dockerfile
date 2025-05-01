FROM centos:latest

WORKDIR /app

RUN yum -y update && \
    yum -y install epel-release && \
    yum -y install vim curl wget net-tools && \
    yum clean all

CMD ["/bin/bash"]
