FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY /scripts/default.conf /etc/nginx/conf.d/