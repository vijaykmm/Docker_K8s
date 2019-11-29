FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y nginx 
RUN mkdir /tmp/docker
RUN touch /tmp/docker/test.txt
RUN touch /tmp/docker/index.html

EXPOSE 80
CMD /usr/sbin/nginx -g "daemon off;"
CMD /usr/sbin/index.html -g "daemon off;"
