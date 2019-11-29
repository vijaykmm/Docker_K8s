FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y Magic-Ball 
RUN mkdir /tmp/docker
RUN touch /tmp/docker/test.txt

EXPOSE 80
CMD /usr/sbin/Magic-Ball -g "daemon off;"
