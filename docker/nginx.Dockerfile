FROM nginx:latest

# Copy the modified nginx.conf
COPY /scripts/nginx.conf /etc/nginx/nginx.conf

# Copy the default.conf
COPY /scripts/default.conf /etc/nginx/conf.d/default.conf