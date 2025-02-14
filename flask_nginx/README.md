# Flask + Nginx

Tree
```bash
flask_nginx/
│── flask/      
│   ├── app.py     
│   ├── requirements.txt
│   ├── Dockerfile 
│── nginx/          
│   ├── nginx.conf    
│   ├── Dockerfile
│── docker-compose.yml
```

Docker Compose
```bash
# Build
$ docker-compose build

# Run container
$ docker-compose up -d

# Quit container
$ docker-compose down
```