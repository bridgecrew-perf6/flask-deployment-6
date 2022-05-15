# flask-deployment

## Traditional way

### Prepare your VM

1. Install Nginx
2. Install Flask

Make sure you open some ports for your app. This tutorial uses port 80 and 8080. 

### Create your apps

Just clone this repo

### Create Gunicorn services

Configure gunicorn as a service 
```
cd /etc/systemd/system
```

Create gunicorn service for app0
```
sudo nano app0.service
```

Type this 
```
[Unit]
Description=Gunicorn service for app0
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/flask-deployment/app0
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:app0.sock -m 007 app0:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Save it and exit

Create gunicorn service for app1
```
sudo nano app1.service
```

Type this 
```
[Unit]
Description=Gunicorn service for app1
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/flask-deployment/app1
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:app1.sock -m 007 app1:app
Restart=always

[Install]
WantedBy=multi-user.target
```
Save it and exit

### Setup Nginx 

Go to nginx folder
```
cd /etc/nginx/sites-enabled
```

Create a new setting 
```
sudo nano app
```

Type this
```
server{
        listen 80;
        #put your public ip address here
        server_name 54.238.205.176;
        location / {
                #proxy_pass http://127.0.0.1:8000;
                proxy_pass /home/ubuntu/flask-deployment/app0/app0.sock;
        }
}


server{
        listen 8080;
        #put your public ip address here
        server_name 54.238.205.176;
        location / {
                #proxy_pass http://127.0.0.1:8000;
                proxy_pass /home/ubuntu/flask-deployment/app1/app1.sock;
        }
}
```

Save it and exit

### Restart all services

```
sudo systemctl daemon-reload
sudo service nginx restart
sudo service app0 restart
sudo service app1 restart
```

### Run it

On your browser, type your public IP address followed by the port. For example:
```
54.238.205.176:80
```

or 
```
54.238.205.176:8080
```

or you can also curl it.
```
curl 54.238.205.176:80
```

or
```
curl 54.238.205.176:8080
```

### Misc

If you encountered error 505, try this but not sure if this a good security practice.
```
chmod o+rx /example_root_folder
```
