FROM debain: latest
RUN apt-get update
RUN apt-get install -y procps vim curl nginx
EXPOSE 80

COPY index.html /usr/share/nginx/html/index.html
CMD /usr/sbin/nginx -g "daemon off;"
