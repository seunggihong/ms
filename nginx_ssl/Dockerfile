FROM nginx:latest

COPY ./path/to/ncsm-test.crt /etc/ssl/certs/
COPY ./path/to/ncsm-test.key /etc/ssl/private/

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]